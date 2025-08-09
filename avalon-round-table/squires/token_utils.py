
# naive token estimate: ~4 chars per token (good enough for budgeting)
def est_tokens(text: str) -> int:
    return max(1, len(text) // 4)

def est_message_tokens(msg: dict) -> int:
    # small overhead for role + formatting
    return 4 + est_tokens(msg.get("content", ""))

def est_total_tokens(messages: list[dict]) -> int:
    return sum(est_message_tokens(m) for m in messages)
