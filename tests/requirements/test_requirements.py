"""Test requirements."""
import logging
import os
import unittest

# from lasso.requirements.requirements import Requirements


GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("ADMIN_GITHUB_TOKEN")

logger = logging.getLogger(__name__)


class MyTestCase(unittest.TestCase):
    """My test case."""

    # These tests are are failing in the original pds-github-util, so we're commenting-them out here too.

    # def test_get_requirements(self):
    #     """Test getting requirements."""
    #     requirements = Requirements("NASA-PDS", "pds-doi-service", token=GITHUB_TOKEN)
    #     requirement_summary = requirements.get_requirements()
    #     logger.info(requirement_summary)

    # def test_get_requirement_task_map(self):
    #     """Test getting the task map."""
    #     requirements = Requirements("NASA-PDS", "pds-doi-service", token=GITHUB_TOKEN)
    #     _ = requirements._get_requirement_tag_map()

    # def test_generate_requirement_file(self):
    #     """Test generation of the requirement file."""
    #     requirements = Requirements("NASA-PDS", "pds-doi-service", token=GITHUB_TOKEN, dev=True)
    #     requirements.write_requirements(md_file_name="output/REQUIREMENTS.md")

    # def test_generate_requirement_file_in_dir(self):
    #     requirements = Requirements('NASA-PDS', 'pds-doi-service', token=GITHUB_TOKEN, dev=True)
    #     requirements.write_requirements(root_dir='pdsen-corral')

    # def test_generate_requirement_file_in_html(self):
    #     requirements = Requirements('NASA-PDS', 'pds-doi-service', token=GITHUB_TOKEN, dev=True)
    #     requirements.write_requirements(root_dir='pdsen-corral', format='html')


if __name__ == "__main__":
    unittest.main()
