import webuiapi

# create API client
api = webuiapi.WebUIApi()

unit1 = webuiapi.ControlNetUnit(input_image=img, module='canny', model='control_canny-fp16 [e3fe7712]')

r = api.txt2img(prompt="photo of a beautiful girl", controlnet_units=[unit1])
r.image