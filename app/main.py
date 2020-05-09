from fastapi import FastAPI
import uvicorn
try:
    from control.tv import Tv
except:
    from .control.tv import Tv

app = FastAPI()
tv = Tv()


@app.post("/volume/{option}", tags=['Volume control'])
def volume(option: str):
    """
    /volume/{option} - Options to control the volume of the TV. \n
    /volume/up - increases the volume of the television. \n
    /volume/down - decreases the volume of the television. \n
    /volume/mute - Mute state

    """
    if option == 'up':
        tv.up_volume()
        return {'volume up'}

    elif option == 'down':
        tv.down_volume()
        return {'volume down'}
    else:
        tv.mute()


@app.post("/channel/{option}", tags=['Channel control'])
def channel(option: str):
    """
    /chan/{option} - This options control channel´s in tv api
    /chan/up - Down channel´s \n
    /chan/down - Down channel´s \n
    """
    if option == 'up':
        try:
            tv.channel_up()
            return {'Channel up'}
        except:
            return {'error!'}
    else:
        tv.channel_down()
        return {'Channel down'}


@app.post("/poweroff", tags=['Turn of TV'])
def poweroff_tv():
    tv.poweroff()
    return {'turning off the tv'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000,
               log_level="info", debug=True)
