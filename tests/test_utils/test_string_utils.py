from pydatadev.utils.string import StringUtils


class TestStringUtils:
    """
    Test suite to test string utility of pydatadev
    """

    def test_strip_and_join(self):
        """
        test strip_and_join string utility function
        :return: None
        """
        str_list = ['/abc/de/fg', 'p/q/rs']
        expected_response = 'abc$de$fg$p$q$rs'

        assert StringUtils.strip_and_join(
            items=str_list,
            connector='$'
        ) == expected_response

    def test_strip_and_get_component_at_index(self):
        """
        test strip_and_get_component_at_index string utility function
        :return: None
        """
        # 'abc/d/e/fg/h', index = 2 == > 'e'
        input_str = 'abc/d/e/fg/h'
        index = 2
        expected_output = 'e'

        assert StringUtils.strip_and_get_component_at_index(
            input_str=input_str,
            index=index
        ) == expected_output

    def test_strip_and_get_components_between_indexes(self):
        """
        test strip_and_get_components_between_indexes string utility function
        :return: None
        """
        input_str = 'abc/de/fg/h/'
        start_index = 1
        expected_result = 'de$fg$h'

        assert StringUtils.strip_and_get_components_between_indexes(
            input_str=input_str,
            start_index=start_index,
            connector='$'
        ) == expected_result
