# 临时demo ,配置已更新，进去全部更新完毕！！

import os
base_path = './Llama-3.1-8B-Instruct-BaJie-Chat'
os.system(f'apt-get install git-lfs')
os.system(f'git clone https://www.modelscope.cn/JimmyMa99/BaJie-Chat-llama3_1-8b.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system(f'cd .. && pip install lmdeploy')
os.system(f'lmdeploy serve gradio {base_path} --model-name llama3 --server-port 7860')
