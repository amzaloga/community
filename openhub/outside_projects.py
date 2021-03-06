import logging

from community.git import get_org_name
from openhub.models import OutsideProject


def get_outside_projects_data(json_object):
    data = json_object['response']['result'
                                   ]['outside_projects']['project']
    return data


def import_data(project):
    logger = logging.getLogger(__name__)
    name = project.get('name', None)

    try:
        project['org'] = get_org_name()
        (c, created) = OutsideProject.objects.get_or_create(
            **project
            )
        if created:
            c.save()
            logger.info('\nOutsideProject %s has been saved' % c)
    except Exception as ex:
        logger.error(
            'Something went wrong saving this OutsideProject %s: %s'
            % (name, ex))
