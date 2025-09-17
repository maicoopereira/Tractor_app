

def machines():
    print("Machines model file.")

class Machines:
    #attributes:
    brand_name = ''
    model_name = ''
    client_name = ''
    series_num = ''
    license_plate = ''
    hour_meter = ''
    service_date = ''
    service_done = ''
    
#constructor
    def __init__(self, brand_name, model_name, client_name, series_num, license_plate, hour_meter, service_date, service_done):
        self.brand_name = brand_name
        self.model_name = model_name
        self.client_name = client_name
        self.series_num = series_num
        self.license_plate = license_plate
        self.hour_meter = hour_meter
        self.service_date = service_date
        self.service_done = service_done

#method to display machine details
    def display_details(self):
        print("Machine Details colected:")
        print(f"Brand Name: {self.brand_name}")
        print(f"Model Name: {self.model_name}")
        print(f"Client Name: {self.client_name}")
        print(f"Series Number: {self.series_num}")
        print(f"License Plate: {self.license_plate}")
        print(f"Hour Meter: {self.hour_meter}")
        print(f"Service Date: {self.service_date}")
        print(f"Service Done: {self.service_done}")
        
#getter and setter methods for each attribute
    def get_brand_name(self):
        return self.brand_name
    def set_brand_name(self, brand_name):
        self.brand_name = brand_name
    def get_model_name(self):
        return self.model_name
    def set_model_name(self, model_name):
        self.model_name = model_name
    def get_client_name(self):
        return self.client_name
    def set_client_name(self, client_name):
        self.client_name = client_name
    def get_series_num(self):
        return self.series_num
    def set_series_num(self, series_num):
        self.series_num = series_num
    def get_license_plate(self):
        return self.license_plate
    def set_license_plate(self, license_plate):
        self.license_plate = license_plate
    def get_hour_meter(self):
        return self.hour_meter
    def set_hour_meter(self, hour_meter):
        self.hour_meter = hour_meter
    def get_service_date(self):
        return self.service_date
    def set_service_date(self, service_date):
        self.service_date = service_date
    def get_service_done(self):
        return self.service_done
    def set_service_done(self, service_done):
        self.service_done = service_done
    
        
        
if __name__ == '__main__':
    machines()
    