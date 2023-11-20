from pydantic import BaseModel

from scraper.models.enums import FilterCodes


class Screener(BaseModel):
    name: str
    filters: dict

    def encode(self) -> str:
        encoded_filters = []
        for key, value in self.filters.items():
            if "x" in FilterCodes[key].value:
                low = value["low"]
                high = value["high"]
                filt = FilterCodes[key].value.replace("x", f"{low}x{high}")
                encoded_filters.append(filt)
            elif "to" in FilterCodes[key].value:
                low = value["low"]
                high = value["high"]
                filt = FilterCodes[key].value.replace("to", f"{low}to{high}")
                encoded_filters.append(filt)
            else:
                filt = FilterCodes[key].value + str(value)
                encoded_filters.append(filt)
        return ",".join(encoded_filters)

    def decode(self) -> str:
        filters = ", ".join([f"{key}: {value}" for key, value in self.filters.items()])
        return f"{self.name}, {filters}"
