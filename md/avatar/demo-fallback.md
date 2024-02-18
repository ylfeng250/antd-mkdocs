## zh-CN

图片不存在时，如果 `src` 本身是个 ReactElement，会尝试回退到 `src`，否则尝试回退到 `icon`，最后回退到显示 `children`。

## en-US

When the image does not exist, if `src` is a ReactElement, it will try to fall back to `src`, otherwise it will try to fall back to `icon`, and finally fall back to displaying `children`.
```tsx
import React from 'react';
import { Avatar, Space } from 'antd';

const App: React.FC = () => (
  <Space>
    <Avatar shape="circle" src="http://abc.com/not-exist.jpg">
      A
    </Avatar>
    <Avatar shape="circle" src="http://abc.com/not-exist.jpg">
      ABC
    </Avatar>
  </Space>
);

export default App;
```
