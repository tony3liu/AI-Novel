from uniai import deepseekChatLLM, zhipuChatLLM

# chatLLM = zhipuChatLLM(model_name="GLM-4", api_key="93c8238ebf3fe2cf702cbc1ce5ec4d1b.xqkKBB72dleCYIjs")
chatLLM = deepseekChatLLM(api_key='sk-39f0e28f0fa940089424d6ceccdeb585')

if __name__ == "__main__":

    content = "请用一个成语介绍你自己"
    messages = [{"role": "user", "content": content}]

    resp = chatLLM(messages)
    print(resp)

    # stream mode
    # for resp in chatLLM(messages, stream=True):
    #     print(resp)
