from typing import List

from pydatadev.constants import DEFAULT_STR_CONNECTOR, DEFAULT_STR_SEPARATOR


class StringUtils:
    """
    Utility class for common String manipulation operations.

    All the functions in this class are ought to be static in nature as :
    no instantiation of StringUtils is intended.
    """

    @staticmethod
    def strip_and_join(items: List[str],
                       separator: str = DEFAULT_STR_SEPARATOR,
                       connector: str = DEFAULT_STR_CONNECTOR) -> str:
        """
        strips all the element of the list based on the separator,
        joins all the sub-element of each element using a connector.

        Example: [ '/abc/de/fg', 'p/q/rs'] ==> 'abcdefgpqrs'

        :param items: list of string elements, List[str]
        :param separator: string which separates sub-elements for an element in the list, str, default = '/'
        :param connector: string which is used to join all the sub-elements of the list, str, default = '/'
        :return: string
        """
        components = []
        for item in items:
            item_components = item.split(separator)
            for x in item_components:
                # remove empty string ''
                if x:
                    components.append(x)

        return connector.join(components)

    @staticmethod
    def strip_and_get_component_at_index(input_str: str,
                                         separator: str = DEFAULT_STR_SEPARATOR,
                                         index: int = 0) -> str:
        """
        Fetches the string at index after splitting the string based on separator

        Example: 'abc/d/e/fg/h', index = 2 ==> 'e'

        :param input_str: string input
        :param separator: string which is used to separate the input_str, str, default = '/'
        :param index: position from which string is to be fetched
        :return: string

        CAUTION : if invalid indexes are wrongly specified then the results can be unexpected
        """
        components = []

        for i in input_str.split(separator):
            # remove empty string ''
            if i:
                components.append(i)

        return components[index]

    @staticmethod
    def strip_and_get_components_between_indexes(input_str: str,
                                                 separator: str = DEFAULT_STR_SEPARATOR,
                                                 connector: str = DEFAULT_STR_CONNECTOR,
                                                 start_index: int = 0,
                                                 end_index: int = None) -> str:
        """
        Creates a string after splitting the original string based on separator.
        Joins the string from start index to end index based on connector.

        Example : 'abc/de/fg/h/', '/' , '/', 1, 2 ==> 'defg'

        :param input_str: string input
        :param separator: string which is used to split input_str, str, default = '/'
        :param connector: string which is used to join the response element between start and end, str, default = '/'
        :param start_index: index from which the string is to be taken in response, int, default = 0
        :param end_index: index until which the string is to be taken in response, int , default = None
        :return: string

        CAUTION : if invalid indexes are wrongly specified then the results can be unexpected
        """
        components = []

        for i in input_str.split(separator):
            # remove empty string ''
            if i:
                components.append(i)

        return connector.join(components[start_index: end_index])
