import requests

# Define the URL and the file paths
url = "https://d544-34-16-163-24.ngrok-free.app/vton/"
person_image_path = "/home/ammar/Desktop/virtual_try_on/woman.png"
cloth_image_path = "cloth overall.png"

# Open the image files
with open(person_image_path, 'rb') as person_img, open(cloth_image_path, 'rb') as cloth_img:
    files = {
        'person_image': person_img,
        'cloth_image': cloth_img,
    }
    data = {
        'cloth_type': 'overall',
        'num_inference_steps': 50,
        'guidance_scale': 2.5,
        'seed': 72,
        'show_type': 'input & result'
    }

    # Send the POST request
    response = requests.post(url, files=files, data=data)

    # Save the result image
    with open("result.png", "wb") as f:
        f.write(response.content)

print("Image saved as result.png")
