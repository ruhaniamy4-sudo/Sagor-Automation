from parser import parse_order_message

def test_valid_order_parsing():
    sample_msg = """
    নাম: রহিম উদ্দিন
    ফোন: 01712345678
    ঠিকানা: মিরপুর ১০, ঢাকা
    দাম: 550
    """
    result = parse_order_message(sample_msg)
    assert result["name"] == "রহিম উদ্দিন"
    assert result["phone"] == "01712345678"
    assert result["address"] == "মিরপুর ১০, ঢাকা"
    assert result["amount"] == 550
