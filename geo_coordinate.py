import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim

class GeocodingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Geocoding Tool")

        self.geolocator = Nominatim(user_agent="geocoding_tool")

        self.create_widgets()

    def geocode_address(self):
        address = self.address_entry.get()
        try:
            location = self.geolocator.geocode(address)
            if location:
                self.result_label.config(text=f"Latitude: {location.latitude}, Longitude: {location.longitude}")
            else:
                self.result_label.config(text="Location not found.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def create_widgets(self):
        # Address Entry
        address_label = tk.Label(self.root, text="Enter Address:")
        address_label.grid(row=0, column=0, padx=10, pady=10)

        self.address_entry = ttk.Entry(self.root)
        self.address_entry.grid(row=0, column=1, padx=10, pady=10)

        # Geocode Button
        geocode_button = ttk.Button(self.root, text="Geocode", command=self.geocode_address)
        geocode_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = GeocodingTool(root)
    root.mainloop()
