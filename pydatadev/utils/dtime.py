from datetime import datetime, date, timedelta, timezone
import time

from pydatadev.constants import DEFAULT_DATETIME_FORMAT, DEFAULT_DATE_FORMAT


class DTimeUtils:
    """
    Utility class comprising static methods which
    """
    @staticmethod
    def get_epoch_with_past_buffer(buffer_in_seconds: int) -> int:
        """
        Get epoch timestamp of past with delta as buffer from the time of invocation
        :param buffer_in_seconds: int, buffer
        :return: int, epoch timestamp of past with delta as buffer
        """
        return int(time.time()) - buffer_in_seconds

    @staticmethod
    def get_epoch_with_future_buffer(buffer_in_seconds: int) -> int:
        """
        Get epoch timestamp of future with delta as buffer from the time of invocation
        :param buffer_in_seconds: int, buffer
        :return: int, epoch timestamp of future with delta as buffer
        """
        return int(time.time()) + buffer_in_seconds

    @staticmethod
    def get_datetime_from_epoch_timestamp(epoch_timestamp: int) -> datetime:
        """
        converts epoch timestamp to datetime object
        :param epoch_timestamp: int
        :return: datetime
        """
        return datetime.fromtimestamp(epoch_timestamp)

    @staticmethod
    def get_datetime_string_from_epoch_timestamp(epoch_timestamp: int,
                                                 dt_format: str = DEFAULT_DATETIME_FORMAT) -> str:
        """
        Get datetime string in a specified format for a given timestamp
        :param epoch_timestamp: int
        :param dt_format: str, defaults to '%Y-%m-%d %H:%M:%S'
        :return: str
        """
        dt_obj = datetime.fromtimestamp(epoch_timestamp).astimezone(timezone.utc)
        return dt_obj.strftime(dt_format)

    @staticmethod
    def get_epoch_timestamp_from_datetime_obj(dt_obj: datetime) -> int:
        """
        convert datetime object to epoch timestamp
        :param dt_obj: datetime object
        :return: int, epoch timestamp
        """
        return int(dt_obj.timestamp())

    @staticmethod
    def get_datetime_obj_from_datetime_encoded_string(dt_str: str,
                                                      dt_format: str = DEFAULT_DATETIME_FORMAT) -> datetime:
        """
        Converts datetime formatted string to datetime object
        :param dt_str: str
        :param dt_format: str, defaults to '%Y-%m-%d %H:%M:%S'
        :return: datetime object
        """
        return datetime.strptime(dt_str, dt_format)

    @staticmethod
    def get_current_datetime_obj_with_second_precision(epoch_timestamp: int,
                                                       dt_format: str = DEFAULT_DATETIME_FORMAT) -> datetime:
        """
        generates datetime object with precision in seconds from the epoch timestamp
        :param epoch_timestamp: int
        :param dt_format: str, defaults to '%Y-%m-%d %H:%M:%S'
        :return: datetime object
        """
        dt_str = DTimeUtils.get_datetime_string_from_epoch_timestamp(epoch_timestamp, dt_format)
        return DTimeUtils.get_datetime_obj_from_datetime_encoded_string(dt_str, dt_format)

    @staticmethod
    def get_current_date_in_str(dt_format: str = DEFAULT_DATE_FORMAT) -> str:
        """
        Generates current date in a string format
        :param dt_format: format of the response datetime srt
        :return: str, date
        """
        today = date.today()
        today_formatted = today.strftime(dt_format)

        return str(today_formatted)

    @staticmethod
    def get_date_str_in_past_with_delta_in_days(dt_str: str,
                                                dt_format: str = DEFAULT_DATE_FORMAT,
                                                delta: int = 1) -> str:
        """
        generates datetime str in the past with deltas as delta days
        :param dt_str: datetime string
        :param dt_format: format of the datetime string
        :param delta: buffer in days, int
        :return: str
        """
        encoded_dt = datetime.strptime(dt_str, dt_format)
        encoded_dt_at_past = encoded_dt - timedelta(days=delta)
        dt_at_past = encoded_dt_at_past.strftime(dt_format)

        return str(dt_at_past)

    @staticmethod
    def get_date_str_in_future_with_delta_in_days(dt_str: str,
                                                  dt_format: str = DEFAULT_DATE_FORMAT,
                                                  delta: int = 1) -> str:
        """
        generates datetime str in the future with deltas as delta days
        :param dt_str: datetime string
        :param dt_format: format of the datetime string
        :param delta: int, buffer in days
        :return: str
        """
        encoded_dt = datetime.strptime(dt_str, dt_format)
        encoded_dt_in_future = encoded_dt + timedelta(days=delta)
        dt_in_future = encoded_dt_in_future.strftime(dt_format)

        return str(dt_in_future)
