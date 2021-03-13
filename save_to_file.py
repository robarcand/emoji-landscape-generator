from generate_land import ask_for_number, generate_land
import os

os.makedirs("landscapes", exist_ok=True)

noise_levels = [1, 5, 10, 20, 50, 100, 250, 500]

for nl in noise_levels:
    output = generate_land(100, 100, nl)

    filename = os.path.join("landscapes", f"noise-levels-{nl}.txt")

    with open(filename, "w") as f:
        f.write(output)