from pyadmitad.items.base import Item

__all__ = (
    'Announcements',
)


class Announcements(Item):
    """
    List of announcements

    Required scope - "announcements"
    """
    URL = Item.prepare_url('announcements')
    SINGLE_URL = Item.prepare_url('announcements/%(id)s')

    def get(self, **kwargs):
        """
        res = client.Announcements.get()
        res = client.Announcements.get(limit=1, offset=2)
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        Here _id is an announcement id

        res = client.Announcements.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)
