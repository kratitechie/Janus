from src.loaders.data_loader import DataLoader
from src.pipeline.router import Router

loader = DataLoader()

router = Router(loader)

output = router.run()

output.to_csv(
    "output.csv",
    index=False
)

print("\n===================================")
print("JANUS COMPLETE")
print("===================================")

print(output.head())