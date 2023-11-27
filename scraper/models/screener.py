from pydantic import BaseModel

from scraper.models.enums import FilterCodes


class Screener(BaseModel):
    name: str
    filters: dict

    def encode(self) -> str:
        encoded_filters = []
        for key, value in self.filters.items():
            code = FilterCodes[key].value
            if code == "earningsdate_x":
                low = value["low"]
                high = value["high"]
                filt = code.replace("x", f"{low}x{high}")
                encoded_filters.append(filt)
            elif code == "ta_topgainers" or code == "ta_toplosers":
                filt = code + str(value)
                encoded_filters.append(filt)
            elif "to" in code:
                low = value["low"]
                high = value["high"]
                filt = code.replace("to", f"{low}to{high}")
                encoded_filters.append(filt)
            else:
                filt = code + str(value)
                encoded_filters.append(filt)
        return ",".join(encoded_filters)

    def decode(self) -> str:
        filters = ", ".join([f"{key}: {value}" for key, value in self.filters.items()])
        return f"{self.name}, {filters}"
