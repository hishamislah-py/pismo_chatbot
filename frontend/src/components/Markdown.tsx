import { memo } from 'react'
import ReactMarkdown, { defaultUrlTransform, type Components } from 'react-markdown'
import { rehypePlugins, remarkPlugins } from '../markdownConfig'
import { safeHref } from '../util'

interface Props {
  content: string
}

const components: Components = {
  a: ({ href, children }) => {
    const safe = safeHref(href)
    return safe ? <a href={safe} target="_blank" rel="noopener noreferrer">{children}</a> : <span>{children}</span>
  },
  // never load remote images from generated text; show the alt text instead
  img: ({ alt }) => <span className="md-img-alt">{alt ? `[image: ${alt}]` : '[image]'}</span>,
  table: ({ children }) => <div className="md-table-wrap"><table>{children}</table></div>,
}

function MarkdownImpl({ content }: Props) {
  return (
    <div className="md">
      <ReactMarkdown
        remarkPlugins={remarkPlugins}
        rehypePlugins={rehypePlugins}
        urlTransform={defaultUrlTransform}
        components={components}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}

export const Markdown = memo(MarkdownImpl)
