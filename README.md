# Drone Plugin Starter (Python)

This repo is a template to writing a drone plugin and is very much based
entirely on [this Golang project template](https://github.com/drone/drone-plugin-starter/).

In fact, a lot of the text in this `README.md` is copy-pasta'd directly from there.

## Usage

Your job could be as simple as:
1. adding custom arguments to be parsed in `src/main.py`
2. adding your custom processing code to `src/myplugin/plugin.py`
3. publishing your plugin and updating the `.drone.yml:publish` step

and you _should_ : 
1. add a `DOCS.md` describing the usage/behavior of your plugin
2. add a nice `logo.svg` to brand your plugin

### Parameters

Plugin parameters are defined in the drone yaml file:

```
slack:
  channel: dev
  username: drone
```

They are prefixed with `PLUGIN_` and sent to the plugin at runtime:

```
PLUGIN_CHANNEL=dev
PLUGIN_USERNAME=drone
```

Outside simply accessing them directly through `os.environ`, these parameters can be 
conveniently exposed and retrieved using `argparse` as seen below:

```
parser.add_argument(
	'--slack-channel',
	default=os.environ.get('PLUGIN_CHANNEL'),
	help='slack channel',
)

parser.add_argument(
	'--slack-username',
	default=os.environ.get('PLUGIN_USERNAME'),
	help='slack username',
)
```

### Secrets

Sensitive fields should not be specified in the yaml file. Instead they are passed to your plugin as environment variable. Secrets should use a prefix that corresponds to the plugin name. For example, the Slack plugin prefixes secrets with `SLACK_`:

```
parser.add_argument(
	'--slack-token',
	default=os.environ.get('SLACK_TOKEN'),
	help='slack token',
)
```

### Logos

Please replace the `logo.svg` file with a meaningful svg logo for your plugin. If you are you building a Slack plugin, for example, please provide the Slack logo. This icon is displayed when your plugin is listed in the official plugin index.

### Docs

Please provide a `DOCS.md` file in the root of your repository that documents plugin usage. This documentation is displayed when your plugin is listed in the official plugin index. Use the `README.md` file to describe building and testing the plugin locally.

### Images

Images are distributed as Docker images in the public Docker registry. Please use a minimalist alpine image when possible to limit the image download size. We are also working on supporting multiple plugin architectures, with compatibility guidelines coming soon

### Testing

Please create plugins that are easily runnable from the command line. This makes it much easier to debug and test plugins locally without having to launch actual builds.
