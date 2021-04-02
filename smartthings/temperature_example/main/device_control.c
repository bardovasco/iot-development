#include "device_control.h"
#include "dht_espidf.h"
#include <esp_err.h>
#include <esp_log.h>

static const char *TEMP_TAG = "temperature_reading";

struct dht_reading read_temp_humidity(void)
{
    struct dht_reading dht_data;

    dht_result_t res = read_dht_sensor_data((gpio_num_t)DHT_IO, DHT11, &dht_data);

    if (res != DHT_OK) {
        ESP_LOGW(TEMP_TAG, "DHT sensor reading failed");
    } else {
        double fahrenheit = (dht_data.temperature * 1.8f) + 32.0f;
        double humidity = dht_data.humidity;
        // ESP_LOGI(TEMP_TAG, "DHT sensor reading: %f° / %f", fahrenheit, humidity);
    }
    return dht_data;
}