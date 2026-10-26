// SVG paths copied from the design prototype.
type P = { className?: string }

function Svg({ className = 'icon', children, filled }: P & { children: React.ReactNode; filled?: boolean }) {
  return (
    <svg viewBox="0 0 20 20" className={className} aria-hidden="true" style={filled ? { fill: 'currentColor', stroke: 'none' } : undefined}>
      {children}
    </svg>
  )
}

export const SidebarIcon = (p: P) => <Svg {...p}><rect x="3" y="4" width="14" height="12" rx="2" /><path d="M8 4v12" /></Svg>
export const PlusIcon = (p: P) => <Svg {...p}><path d="M10 4v12M4 10h12" /></Svg>
export const SearchIcon = (p: P) => <Svg {...p}><circle cx="9" cy="9" r="5.5" /><path d="M13 13l4 4" /></Svg>
export const DotsIcon = (p: P) => <Svg {...p} filled><circle cx="5" cy="10" r="1.4" /><circle cx="10" cy="10" r="1.4" /><circle cx="15" cy="10" r="1.4" /></Svg>
export const TrashIcon = (p: P) => <Svg {...p}><path d="M4 6h12M8 6V4h4v2M6 6l1 10h6l1-10" /></Svg>
export const ChatIcon = (p: P) => <Svg {...p}><path d="M4 4.5h12a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5H9l-4 3v-3H4A1.5 1.5 0 0 1 2.5 13V6A1.5 1.5 0 0 1 4 4.5z" /></Svg>
export const ArrowOutIcon = (p: P) => <Svg {...p}><path d="M7 13l6-6M8 7h5v5" /></Svg>
export const CopyIcon = (p: P) => <Svg {...p}><rect x="7" y="7" width="9" height="9" rx="1.5" /><path d="M13 7V5.5A1.5 1.5 0 0 0 11.5 4h-6A1.5 1.5 0 0 0 4 5.5v6A1.5 1.5 0 0 0 5.5 13H7" /></Svg>
export const WarnIcon = (p: P) => <Svg {...p}><path d="M10 3l8 14H2z" /><path d="M10 8v4M10 14.5v.01" /></Svg>
export const RetryIcon = (p: P) => <Svg {...p}><path d="M4 10a6 6 0 1 0 2-4.5" /><path d="M4 3v3.5h3.5" /></Svg>
export const SendIcon = (p: P) => <Svg {...p}><path d="M10 16V4M5 9l5-5 5 5" /></Svg>
export const CloseIcon = (p: P) => <Svg {...p}><path d="M5 5l10 10M15 5L5 15" /></Svg>
export const ExternalIcon = (p: P) => <Svg {...p}><path d="M8 4H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-3" /><path d="M11 4h5v5M16 4l-7 7" /></Svg>
