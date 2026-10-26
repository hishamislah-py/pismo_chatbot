---
ku_id: KU-CARD-pinpinblock-tutorial
title: PIN/PINBlock tutorial
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/pinpinblock-tutorial.md
  sha256: ec26af04451e4e557e592e20ea65f3432c78cf67c03ef1df966385d93541324c
  url: https://developers.pismo.io/pismo-docs/docs/pinpinblock-tutorial
  role: primary_guide
  updated_at: '2026-03-18T15:21:49.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# PIN/PINBlock tutorial

**KU ID:** `KU-CARD-pinpinblock-tutorial` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/pinpinblock-tutorial.md`:

> a PIN ready for encryption and secure transmission in banking networks.</p>

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/pinpinblock-tutorial.md`: PIN/PINBlock tutorial

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/pinpinblock-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pinpinblock-tutorial · updatedAt: 2026-03-18T15:21:49.000Z

<!-- source:begin path=docs/card-issuing/pinpinblock-tutorial.md part=0-end -->

# PIN/PINBlock tutorial

<HTMLBlock>
  {`
  <p>For clients who don't want a PIN (Personal Identification Number) transmitted as clear text, Pismo can handle it in PINBlock format. PINBlocks are 64-bit strings that encode
      a PIN ready for encryption and secure transmission in banking networks.</p>
  <p>In this tutorial, without a <a href="https://en.wikipedia.org/wiki/Hardware_security_module" target="_blank">Hardware Security Module</a> (HSM), you are going to decrypt a PINBlock to get a clear text PIN and update a PIN using a PINBlock. 
        The example code is written in Javascript and uses an external library called <a href="https://www.npmjs.com/package/crypto-js" target="_blank">CryptoJS</a> to 
        support <a href="https://en.wikipedia.org/wiki/Triple_DES" target="_blank">3DES</a> operations.</p>
  <p>This tutorial assumes you have some familiarity with Node.js, Postman (a tool used for making API calls), and running commands at the command-line.</p>
    
    <p>For this tutorial you need:</p>
    <ul>
      <li><a href="https://www.postman.com/downloads/" target="_blank">Postman</a></li>
      <li><a href="https://nodejs.org/en/download/" target="_blank">Node.js</a></li>
      <li><a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm" target="_blank">npm</a></li>
      <li> A server key and server secret for use in the Pismo sandbox environment in Postman</li>
      <li>One credit program to create a card</li>
    </ul>

  <p><b>PIN/PINBlock endpoints</b></p>
  <ul>
    <li><p><a href="https://developers.pismo.io/pismo-docs/reference/get-v1-pin-as-pinblock" target="_blank">Get PIN as PINBlock</a></p></li>
    <li><p><a href="https://developers.pismo.io/pismo-docs/reference/put-v1-update-pin-from-pinblock" target="_blank">Update PIN from PINBlock</a></p></li>
  </ul>
    
    <p><b>To test Pismo PINBlock endpoints:</b></p>
    <ol>
      <li><p>Create a tutorial directory</p>
        <p><code> &gt; mkdir pismo-pin</code><br>
        <code> &gt; cd pismo-pin</code></p>
      </li>
      <li><p>Download <a href="https://pismoassets.pismo.io/pismo-docs/PCIPINSecResources.zip"><b>PCIPINSecResources.zip</b></a> and extract it to the tutorial directory<br></p>
      </li>
        <li><p>Install NPM dependencies</p>
        <p><code> &gt; npm install</code></p>
      </li>
      <li><p>Open Postman and import the collection file. Use the Sandbox environment.</p></li>
      <li><p>Edit the collection variables with values for <code>server_key</code>, <code>server_secret</code>, and <code>program_ID</code></p></li>
      <li><p>Execute Postman requests until you reach <b>7 - Get PIN as pinblock</b></p></li>
      <li><p>Decrypt the PINBlock to retrieve the clear PIN</p>
      <p>For this, use the JavaScript code downloaded in the second step. Run the following command:</p>
      <p><code> &gt; node index.js decryptPinblock "&lt;PINBlock&gt;" "&lt;PAN&gt;" "&lt;Clear ZPK&gt;"</code></p>
      <p>For example:</p>
      <pre>&gt; node index.js decryptPinblock "D04BCCEE7133CF01" "1234560057855917" "0404F2543B1C6E70AB61586E1304B6A7"</pre>
      <p>Example output:</p>
      <pre>see the plain text of the pinblock 0449c39ffa87aa6e
  see the pinblock part1 044986FFFFFFFFFF
  Plain PIN 4986
  --------make-runnable-output--------
  4986</pre>
      <p>In a sandbox environment, a fixed ZPK (Zone Pin Key) is used where the value is <code>0404F2543B1C6E70AB61586E1304B6A7</code>. In production, 
          the Pismo security team generates this ZPK and sends it to you.</p>
      </li>
      <li><p>Update the card PIN using a PINBlock</p>
      <p>Select a new PIN like "1234” and use it to generate a PINBlock  using JavaScript:</p>
      <p><code>&gt; node index.js encryptPinblock "&lt;NEW PIN&gt; "&lt;PAN&gt;" "&lt;Clear ZPK&gt;"</code></p>
      <p>For example:</p>
      <pre>&gt; node index.js encryptPinblock "1234" "1234560057855917" "0404F2543B1C6E70AB61586E1304B6A7" </pre>
      <p>Example output:</p>
      <pre>pinblock 577E22088DE3AA1E
  --------make-runnable-output--------
  577E22088DE3AA1E</pre>
       </li>
      <li><p>Run the Postman request <b>8 - Update PIN from PINBlock</b></p>
      <p>You can reproduce the last step to retrieve the PIN as PINBlock and decrypt it to verify that the PIN has changed.</p></li>
    </ol>

      <p>The index.js program uses CryptoJS, but you can code your own version of this using libraries that support 3DES in the most popular programming languages such as:</p>
      
      <ul><li><a href="https://docs.oracle.com/javase/7/docs/api/javax/crypto/package-summary.html" target="_blank">Java</a></li>
      <li><a href="https://docs.microsoft.com/pt-br/dotnet/api/system.security.cryptography.tripledes?view=net-5.0" target="_blank">C#</li> 
      <li><a href="https://pkg.go.dev/crypto/des" target="_blank">Golang</a></li> 
      <li><a href="https://www.npmjs.com/package/crypto-js" target="_blank">Javascript</a></li> 
      <li><a href="https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html" target="_blank">Python</a></li> 
  </ul>
           
      <p><b>Note:</b> During implementation, remember to always convert the ZPK and PINBlocks to uppercase.</p>
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/pinpinblock-tutorial.md`: updatedAt 2026-03-18T15:21:49.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/pinpinblock-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pinpinblock-tutorial | `ec26af04451e4e55…` | 2026-03-18T15:21:49.000Z |

## Related knowledge units

- None.
