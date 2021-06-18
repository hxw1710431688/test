from streamlit_webrtc import ClientSettings

DIR_PATH = './'
input_videos = '/data/'
output_video = 'output/output_video.mp4'
OUTPUT_PATH = DIR_PATH + output_video
INPUT_PATH = DIR_PATH+ input_videos
VIDEO_PATH = DIR_PATH + input_videos

CLASSES = ['限速20','限速30','限速50','限速60','限速70','限速80','解除限制80','限速100','限速120','禁止超车','禁止总重量超过3.5T的车辆超车','优先行使','干道先行','让路','停止','道路封闭','超过2-3.5T车辆禁止进入',
'禁止所有车辆进入','危险','曲线（左）','曲线（右）','变曲线','道路颠簸','地面湿滑','右侧车道缩减','道路工程','前方有交通信号灯',
'注意行人','当心儿童','禁止自行车进入','当心霜雪','小心野生动物','结束限制','右转','左转','直行','右转或直行','左转或直行',
'右侧通行','左侧通行','环岛绕行','解除禁止超车','解除禁止总重量超过3.5T的车辆超车']

WEBRTC_CLIENT_SETTINGS = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
    )
