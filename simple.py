from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID =  "GOZmY9F7ttZiAU6scT7gdeJSLAni03fnwfoUmML8"
CLARIFAI_APP_SECRET = "8KQ-rU_xyFAHErVDZb31a3CvSt2p3dcAvKipLYbt"
app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)

model = app.models.get("general-v1.3")

result = model.predict_by_url(url='http://dogfriendlydirectory.com/wp-content/uploads/photo-gallery/cute-dog-pictures-for-kids.jpg')

print(result["outputs"][0]["input"])

concept_list = result["outputs"][0]["data"]["concepts"]
for concept in concept_list:
    print(str(concept["value"]) + "\t"+ concept["name"])
