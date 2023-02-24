## To configure (ubuntu 22.04)

Clone the git repo...

Add `LOCAL.env` to the directory with these values:

    OPENAI_API_KEY=
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_DEFAULT_REGION=

The OpenAI key comes from their site

The AWS info comes from creating an IAM user with the `AmazonTextractFullAccess` canned policy.


## To build it

`sudo apt install gnome-screenshot`
`./build`

## To run it

`./run-with-cap`

## Not using ubuntu?

Create a file `input.png` and then call `./run`




