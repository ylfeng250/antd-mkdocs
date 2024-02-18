## zh-CN

调试用组件，请勿直接使用。

## en-US

Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { Mentions } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalMentions } = Mentions;

const options = [
  {
    value: 'afc163',
    label: 'afc163',
  },
  {
    value: 'zombieJ',
    label: 'zombieJ',
  },
];

const App: React.FC = () => (
  <InternalMentions style={{ width: '100%' }} value="@" options={options} />
);

export default App;
```
