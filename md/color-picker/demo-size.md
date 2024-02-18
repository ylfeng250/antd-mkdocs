## zh-CN

触发器有大、中、小三种尺寸，若不设置 size，则尺寸为中。

## en-US

The trigger has three sizes: large, medium and small. If size is not set, the size will be medium.
```tsx
import React from 'react';
import { ColorPicker, Space } from 'antd';

const Demo = () => (
  <Space>
    <Space direction="vertical">
      <ColorPicker defaultValue="#1677ff" size="small" />
      <ColorPicker defaultValue="#1677ff" />
      <ColorPicker defaultValue="#1677ff" size="large" />
    </Space>
    <Space direction="vertical">
      <ColorPicker defaultValue="#1677ff" size="small" showText />
      <ColorPicker defaultValue="#1677ff" showText />
      <ColorPicker defaultValue="#1677ff" size="large" showText />
    </Space>
  </Space>
);

export default Demo;
```
