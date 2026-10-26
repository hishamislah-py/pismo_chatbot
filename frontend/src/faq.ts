// Curated demo questions (2026-10-23). Each was kept only after checking the evidence retrieved for that exact wording
// and asking it live. Questions whose evidence was incomplete or scattered, or whose live answer mixed up endpoints,
// were replaced (PCI card go-live, which is not documented; a general "platform events" question; and the broader
// "How do I cancel a transfer(, and which API ...)?", whose live answers attributed one endpoint's details to the other).
// `topic` is only a navigation label for the FAQ list; it says nothing about what the documentation covers.
export const FAQ: readonly { topic: string; question: string }[] = [
  { topic: 'Webhooks', question: 'How do I verify Pismo webhook requests in production?' },
  { topic: 'Transfers', question: 'How do I create a transfer using the Payment methods API?' },
  { topic: 'Transfers', question: 'How do I cancel a transfer using the Payment methods API?' },
  { topic: 'Transfers', question: 'How do I create and confirm a pre-authorized transfer?' },
  { topic: 'Authentication', question: 'How do I get an OpenID Connect access token for the Pismo APIs?' },
  { topic: 'Events', question: 'Which event is generated when I create a transfer?' },
]
