// Markdown plugin configuration shared by components/Markdown.tsx and the Node tests (no JSX here).
import type { Options } from 'react-markdown'
import rehypeSanitize, { defaultSchema } from 'rehype-sanitize'
import remarkGfm from 'remark-gfm'
import { remarkHideCitations } from './citations.ts'
import { rehypePresentation, remarkLiteralHtml } from './markdownPresentation.ts'

// Raw HTML in answers is never rendered: remarkLiteralHtml turns it into literal text first (so placeholders such as
// <Production Domain> stay visible), and rehype-sanitize filters the resulting tree against GitHub's allow-list.
// Evidence markers ([E1]) are left out of the prose (remarkHideCitations); each answer's Sources section lists its
// citations. rehypePresentation runs after sanitizing.
export const sanitizeSchema = defaultSchema

export const remarkPlugins: Options['remarkPlugins'] = [remarkGfm, remarkLiteralHtml, remarkHideCitations]
export const rehypePlugins: Options['rehypePlugins'] = [[rehypeSanitize, sanitizeSchema], rehypePresentation]
