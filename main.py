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

parallel_model = unetNorm()
model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
parallel_model.fit_generator(myGene,steps_per_epoch=30,epochs=2000,callbacks=[model_checkpoint])

testGene = testGenerator("data/JOSM/test")
parallel_model = unetNorm()
parallel_model.load_weights("unet_membrane.hdf5")
results = parallel_model.predict_generator(testGene,1,verbose=1)
saveResult("data/JOSM/result",results)