def get_time(formato):
    from datetime import datetime, tzinfo, timedelta

    class TZ(tzinfo):
        def utcoffset(self, dt):
            return timedelta(hours=+1)

        def dst(self, _):
            return timedelta(0)

        def tzname(self, _):
            return

    return datetime.now(TZ()).strftime(formato)