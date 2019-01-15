from argparse import ArgumentParser
from distutils.util import strtobool
from os import environ as ENV


def attach_drone_args_parsing(parser=None):
    if not parser:
        parser = ArgumentParser()

    # repo args

    parser.add_argument('--repo',
                        type=str,
                        dest='repo_fullname',
                        help='repository full name',
                        default=ENV.get('DRONE_REPO'))

    parser.add_argument('--repo-owner',
                        type=str,
                        dest='repo_owner',
                        help='repository owner',
                        default=ENV.get('DRONE_REPO_OWNER'))

    parser.add_argument('--repo-name',
                        type=str,
                        dest='repo_name',
                        help='repository name',
                        default=ENV.get('DRONE_REPO_NAME'), )

    parser.add_argument('--repo-link',
                        type=str,
                        dest='repo_link',
                        help='repository link',
                        default=ENV.get('DRONE_REPO_LINK'))

    parser.add_argument('--repo-avatar',
                        type=str,
                        dest='repo_avatar',
                        help='repository avatar',
                        default=ENV.get('DRONE_REPO_AVATAR'))

    parser.add_argument('--repo-branch',
                        type=str,
                        dest='repo_branch',
                        help='repository default branch',
                        default=ENV.get('DRONE_REPO_BRANCH'))

    parser.add_argument('--repo-private',
                        type=strtobool,
                        dest='repo_private',
                        help='repository is private',
                        default=ENV.get('DRONE_REPO_PRIVATE', False))

    parser.add_argument('--repo-trusted',
                        type=bool,
                        dest='repo_trusted',
                        help='repository is trusted',
                        default=ENV.get('DRONE_REPO_TRUSTED'))

    # commit args

    parser.add_argument('--remote-url',
                        type=str,
                        dest='remote_url',
                        help='git remote url',
                        default=ENV.get('DRONE_REMOTE_URL'))

    parser.add_argument('--commit-sha',
                        type=str,
                        dest='commit_sha',
                        help='git commit sha',
                        default=ENV.get('DRONE_COMMIT_SHA'))

    parser.add_argument('--commit-ref',
                        type=str,
                        dest='commit_ref',
                        help='git commit ref',
                        default=ENV.get('DRONE_COMMIT_REF',
                                        'refs/heads/master'))

    parser.add_argument('--commit-branch',
                        type=str,
                        dest='commit_branch',
                        help='git commit branch',
                        default=ENV.get('DRONE_COMMIT_BRANCH', 'master'))

    parser.add_argument('--commit-message',
                        type=str,
                        dest='commit_message',
                        help='git commit message',
                        default=ENV.get('DRONE_COMMIT_MESSAGE'))

    parser.add_argument('--commit-link',
                        type=str,
                        dest='commit_link',
                        help='git commit link',
                        default=ENV.get('DRONE_COMMIT_LINK'))

    parser.add_argument('--commit-author',
                        type=str,
                        dest='commit_author_name',
                        help='git author name',
                        default=ENV.get('DRONE_COMMIT_AUTHOR'))

    parser.add_argument('--commit-author-email',
                        type=str,
                        dest='commit_author_email',
                        help='git author email',
                        default=ENV.get('DRONE_COMMIT_AUTHOR_EMAIL'))

    parser.add_argument('--commit-author-avatar',
                        type=str,
                        dest='commit_author_avatar',
                        help='git author avatar',
                        default=ENV.get('DRONE_COMMIT_AUTHOR_AVATAR'))

    # build args

    parser.add_argument('--build-event',
                        type=str,
                        dest='build_event',
                        help='build event',
                        default=ENV.get('DRONE_BUILD_EVENT', 'push'))

    parser.add_argument('--build-number',
                        type=int,
                        dest='build_number',
                        help='build number',
                        default=ENV.get('DRONE_BUILD_NUMBER'))

    parser.add_argument('--build-created',
                        type=int,
                        dest='build_created',
                        help='build created',
                        default=ENV.get('DRONE_BUILD_CREATED'))

    parser.add_argument('--build-started',
                        type=int,
                        dest='build_started',
                        help='build started',
                        default=ENV.get('DRONE_BUILD_STARTED'))

    parser.add_argument('--build-finished',
                        type=int,
                        dest='build_finished',
                        help='build finished',
                        default=ENV.get('DRONE_BUILD_FINISHED'))

    parser.add_argument('--build-status',
                        type=str,
                        dest='build_status',
                        help='build status',
                        default=ENV.get('DRONE_BUILD_STATUS', 'status'))

    parser.add_argument('--build-link',
                        type=str,
                        dest='build_link',
                        help='build link',
                        default=ENV.get('DRONE_BUILD_LINK'))

    parser.add_argument('--deploy-to',
                        type=str,
                        dest='build_deploy',
                        help='build deployment dest',
                        default=ENV.get('DRONE_DEPLOY_TO'))

    parser.add_argument('--yaml-verified',
                        type=strtobool,
                        dest='yaml_verified',
                        help='build yaml is verified',
                        default=ENV.get('DRONE_YAML_VERIFIED', False))

    parser.add_argument('--yaml-signed',
                        type=strtobool,
                        dest='yaml_signed',
                        help='build yaml is signed',
                        default=ENV.get('DRONE_YAML_SIGNED', False))

    # prev build args

    parser.add_argument('--prev-build-number',
                        type=int,
                        dest='prev_build_number',
                        help='previous build number',
                        default=ENV.get('DRONE_PREV_BUILD_NUMBER', -1))

    parser.add_argument('--prev-build-status',
                        type=str,
                        dest='prev_build_status',
                        help='previous build status',
                        default=ENV.get('DRONE_PREV_BUILD_STATUS'))

    parser.add_argument('--prev-commit-sha',
                        type=str,
                        dest='prev_commit_sha',
                        help='previous build sha',
                        default=ENV.get('DRONE_PREV_COMMIT_SHA'))

    return parser
