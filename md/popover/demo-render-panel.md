## zh-CN

调试用组件，请勿直接使用。

## en-US

Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { Popover } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalPopover } = Popover;

const content = (
  <div>
    <p>Content</p>
    <p>Content</p>
  </div>
);

const App: React.FC = () => (
  <>
    <InternalPopover content={content} title="Title" />
    <InternalPopover
      content={content}
      title="Title"
      placement="bottomLeft"
      style={{ width: 250 }}
    />
  </>
);

export default App;
```
