import os
from torchvision.models import resnet50, ResNet50_Weights
import torchvision.transforms as Transforms
from PIL import Image

basedir = os.path.abspath(os.path.dirname(__file__))

def image_detector(image):
	img = Image.open(image)
	transforms = Transforms.Resize(250)
	transform_img = transforms(img)
	transform_img.save(f"{os.path.join(basedir, 'uploads')}/transform_img.jpeg", format="jpeg")
	# Step 1: Initialize model with the best available weights
	weights = ResNet50_Weights.DEFAULT
	model = resnet50(weights=weights)
	model.eval()
	# Step 2: Initialize the inference transforms
	preprocess = weights.transforms()
	# Step 3: Apply inference preprocessing transforms
	batch = preprocess(transform_img).unsqueeze(0)
	# Step 4: Use the model and print the predicted category
	prediction = model(batch).squeeze(0).softmax(0)
	class_id = prediction.argmax().item()
	score = prediction[class_id].item()
	category_name = weights.meta["categories"][class_id]
	# print(f"{category_name}: {100 * score:.1f}%")
	# print(f"Image size (height: {img.size[1]}, width: {img.size[0]})")
	return img.size[1], img.size[0], "transform_img.jpeg", category_name, f"{100 * score: .1f}"


if __name__ == "__main__":
	image_detector("test_dog_7796ba9d41.jpg")
