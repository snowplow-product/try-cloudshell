# Try Snowplow

## Select a project

You will deploy Try Snowplow into your chosen GCP project.  You can use an existing project or create a new one, but you must have billing enabled.

<walkthrough-project-setup billing="true"></walkthrough-project-setup>

## Set your input parameters

You need to set some configuration parameters to customise your TrySnowplow pipeline.

Open the <walkthrough-editor-open-file filePath="./inputs.yaml">inputs.yaml</walkthrough-editor-open-file> file and edit the parameters.


## Launch your pipeline

If you are happy with your configuration parameters, then it is time to deploy your pipeline.

Copy this command into the terminal shell and hit return:

```sh
./deploy-try-snowplow {{project-id}}
```

That command runs a script that launches your pipeline infrasture in your GCP project.

The script takes a few minutes to run.  Lookout for the "Success!!" message in the console, which tells you your pipeline is ready.

## Start tracking

You have deployed your pipeline.  Head over to [Try Snowplow](https://try.snowplowanalytics.com/) to learn how to start tracking events.

## Tear down your pipeline

To destroy your pipeline, head to [the deployent manager console](https://console.cloud.google.com/dm/deployments) and make sure you are listing deployments for project "{{ project-id }}".  Select your snowplow deployment and click "Delete".
