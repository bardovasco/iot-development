#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "st_dev.h"
#include "dht_espidf.h"
#include "device_control.h"
#include "dht_espidf.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

// onboarding_config_start is null-terminated string
extern const uint8_t onboarding_config_start[] asm("_binary_onboarding_config_json_start");
extern const uint8_t onboarding_config_end[] asm("_binary_onboarding_config_json_end");
// device_info_start is null-terminated string
extern const uint8_t device_info_start[]    asm("_binary_device_info_json_start");
extern const uint8_t device_info_end[]        asm("_binary_device_info_json_end");

static iot_status_t g_iot_status = IOT_STATUS_IDLE;
static iot_stat_lv_t g_iot_stat_lv;

IOT_CTX* ctx = NULL;

/*
 * Capability Initialization
 * and futher handling.
 * */
// static caps_button_data_t *cap_button_data;

static void capability_init()
{
    // Capability initializer
}

/*
 * SmartThings Connection Handlers
 *    @iot_status_cb
 *    @connection_start
 *    @iot_noti_cb
 **/
static void iot_status_cb(iot_status_t status,
                          iot_stat_lv_t stat_lv, void *usr_data)
{
    g_iot_status = status;
    g_iot_stat_lv = stat_lv;

    printf("status: %d, stat: %d\n", g_iot_status, g_iot_stat_lv);
}

static void connection_start(void)
{
    iot_pin_t *pin_num = NULL;
    int err;

#if defined(SET_PIN_NUMBER_CONFRIM)
    pin_num = (iot_pin_t *) malloc(sizeof(iot_pin_t));
    if (!pin_num)
        printf("failed to malloc for iot_pin_t\n");

    //[>to decide the pin confirmation number(ex. "12345678"). It will use for easysetup.<]
    // pin confirmation number must be 8 digit number.
    pin_num_memcpy(pin_num, "12345678", sizeof(iot_pin_t));
#endif

     //process on-boarding procedure. There is nothing more to do on the app side than call the API.
    err = st_conn_start(ctx, (st_status_cb)&iot_status_cb, IOT_STATUS_ALL, NULL, pin_num);
    if (err) {
        printf("fail to start connection. err:%d\n", err);
    }
    if (pin_num) {
        free(pin_num);
    }
}

static void iot_noti_cb(iot_noti_data_t *noti_data, void *noti_usr_data)
{
    printf("Notification message received\n");

    if (noti_data->type == IOT_NOTI_TYPE_DEV_DELETED) {
        printf("[device deleted]\n");
    } else if (noti_data->type == IOT_NOTI_TYPE_RATE_LIMIT) {
        printf("[rate limit] Remaining time:%d, sequence number:%d\n",
               noti_data->raw.rate_limit.remainingTime, noti_data->raw.rate_limit.sequenceNumber);
    }
}

void temp_task(void)
{
    struct dht_reading dht_data;

    while (1){
        dht_data = read_temp_humidity();

        printf("temperature: %f°, humidity: / %f",
            dht_data.temperature,
            dht_data.humidity);
        vTaskDelay(pdMS_TO_TICKS(TEMP_READING_DELAY));
    }
}

void app_main(void)
{
    unsigned char *onboarding_config = (unsigned char *) onboarding_config_start;
    unsigned int onboarding_config_len = onboarding_config_end - onboarding_config_start;
    unsigned char *device_info = (unsigned char *) device_info_start;
    unsigned int device_info_len = device_info_end - device_info_start;

    int iot_err;

    /*
     * Initialize context
     * */
    ctx = st_conn_init(
        onboarding_config,
        onboarding_config_len,
        device_info,
        device_info_len);

    if (ctx != NULL) {
        iot_err = st_conn_set_noti_cb(ctx, iot_noti_cb, NULL);
        if (iot_err)
            printf("fail to set notification callback function\n");
    } else {
        printf("fail to create the iot_context\n");
    }

    /*
     * Capability and GPIO Config Init
     **/
    capability_init();

    /*
     * Register Tasks
     * */
    xTaskCreate(temp_task, "temp_task", 4096, NULL, 10, NULL);

    // connect to server
    connection_start();
}
