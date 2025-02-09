from model import *
from data import *

#os.environ["CUDA_VISIBLE_DEVICES"] = "2"


data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(2,'data/JOSM/train','image','label',data_gen_args,save_to_dir = None)

model = unetNorm()
model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=50,epochs=5000,callbacks=[model_checkpoint])

testGene = testGenerator("data/JOSM/test")
model = unetNorm()
model.load_weights("unet_membrane.hdf5")
results = model.predict_generator(testGene,20,verbose=1)
saveResult("data/JOSM/result",results)
