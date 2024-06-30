import discord 
from discord.ext import commands
import uTube
import os
import boto3
from openai import AsyncOpenAI
import requests


class AudioPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.VoiceChannel = None
        self.song_playing = None

    @commands.command(name="join")
    async def join(self, ctx):
        #await ctx.message.channel.send(ctx.message.author.voice.channel)
        channel = ctx.message.author.voice.channel
        self.VoiceChannel = await channel.connect()
        #voiceChannel.play(discord.FFmpegPCMAudio(source="Saruman the Stupid [fOx7gFwE1oU].m4a"))

    @commands.command(name="leave")
    async def leave(self, ctx):
        await ctx.guild.voice_client.disconnect()
        self.VoiceChannel = None

    @commands.command(name="play")
    async def search(self, ctx, term):

        split = term.split("/")
        code = split[len(split) - 1].split("=")
        title = code[len(code)-1]
        print(title)
        uTube.lookup_video(term, title)
        await ctx.message.reply("playing {}".format(term))
        self.VoiceChannel.play(discord.FFmpegPCMAudio(source=title+".m4a"))


    @commands.command(name="stop")
    async def stop(self, ctx):
        if self.song_playing:
            print("guh")
        else:
            print("guh")

    @commands.command(name="tts")
    async def request_systhesis(self, ctx, args):
        polly_client = boto3.Session(aws_access_key_id='AKIAXXWLCTEWJMNV2QPZ',aws_secret_access_key='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', region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Brian',
                OutputFormat='mp3', 
                Text = ctx.message.content[5:],
                Engine = 'neural')

        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()

        self.VoiceChannel.play(discord.FFmpegPCMAudio(source='speech.mp3'))


    @commands.command(name="gpt")
    async def request_gpt(self, ctx, args):
        message = ctx.message.content[5:]
        engine = "gpt-3.5-turbo-16k"
        temp = 1
        tokens = 16000

        System_prompt = "you are a AI Chatbot, and will do your best to roleplay given scenarios or prompts, your base name is 'adrian-bot' if you havent been given a prompt or are just asked a question. when asked a question, try your best to fulfil it accuratelyt but occasionally get the information completely wrong"

        client = AsyncOpenAI(
            api_key="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"
        )

        response = await client.chat.completions.create(
            model=engine,
            messages=[
                {
                    "role": "system", "content": System_prompt#"You are a robotic assistant called 'Adrian-bot', and you can answer any question in the world but somewhat poorly"
                },
                {
                    "role": "user", "content": message
                }
            ],
            temperature= temp,
            stop=None,
            max_tokens= tokens
        )
        reply = response.choices[0].message.content
        
        polly_client = boto3.Session(aws_access_key_id='AKIAXXWLCTEWJMNV2QPZ',aws_secret_access_key='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', region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Brian',
                OutputFormat='mp3', 
                Text = reply,
                Engine = 'neural')

        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()

        await ctx.message.reply(reply)
        self.VoiceChannel.play(discord.FFmpegPCMAudio(source='speech.mp3'))

    @commands.command(name="gpti")
    async def request_gpti(self, ctx, args):
        try:
            message = ctx.message.content[6:]
            client = AsyncOpenAI(api_key="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")
            
            response = await client.images.generate(
            model="dall-e-3",
            prompt=message,
            size="1024x1024",
            quality="standard",
            n=1,
            )

            image_url = response.data[0].url
            img_data = requests.get(image_url)
            with open('temp.png', "wb") as f:
                f.write(img_data.content)
            await ctx.channel.send(message, file=discord.File('temp.png'))
        except :
            await ctx.message.reply("uhhhhhhhh something went wrong")
