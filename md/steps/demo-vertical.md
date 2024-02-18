## zh-CN

简单的竖直方向的步骤条。

## en-US

A simple step bar in the vertical direction.
```tsx
import React from 'react';
import { Steps } from 'antd';

const description = 'This is a description.';
const App: React.FC = () => (
  <Steps
    direction="vertical"
    current={1}
    items={[
      {
        title: 'Finished',
        description,
      },
      {
        title: 'In Progress',
        description,
      },
      {
        title: 'Waiting',
        description,
      },
    ]}
  />
);

export default App;
```
