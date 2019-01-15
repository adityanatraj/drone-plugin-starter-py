import logging

from drone.args import attach_drone_args_parsing
from myplugin.custom import run_my_plugin


if __name__ == '__main__':
    parser = attach_drone_args_parsing()

    parser.add_argument(
        '--verbose',
        action='store_true',
        default=False,
        help='turn on debug logging'
    )

    # add your custom arguments to be parsed from the `settings` key,
    # remember to set default from the expected environment variable:
    # PLUGIN_{CAPS_UNDERSCORED_ARG_NAME}
    # ex:
    #     parser.add_argument(
    #         '--my-first-arg',
    #         default=os.environ.get('PLUGIN_MY_FIRST_ARG'),
    #         help='my first custom argument'
    #     )

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(f'got args: {args}')

    run_my_plugin(args)
