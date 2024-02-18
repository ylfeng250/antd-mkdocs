## zh-CN

渲染触发器的默认文本, `showText` 为 `true` 时生效。自定义文本时，可以使用 `showText` 为函数的方式，返回自定义的文本。

## en-US

Renders the default text of the trigger, effective when `showText` is `true`. When customizing text, you can use `showText` as a function to return custom text.
```tsx
import React, { useState } from 'react';
import { DownOutlined } from '@ant-design/icons';
import { ColorPicker, Space } from 'antd';

const Demo = () => {
  const [open, setOpen] = useState(false);
  return (
    <Space direction="vertical">
      <ColorPicker defaultValue="#1677ff" showText />
      <ColorPicker
        defaultValue="#1677ff"
        showText={(color) => <span>Custom Text ({color.toHexString()})</span>}
      />
      <ColorPicker
        defaultValue="#1677ff"
        open={open}
        onOpenChange={setOpen}
        showText={() => (
          <DownOutlined
            rotate={open ? 180 : 0}
            style={{
              color: 'rgba(0, 0, 0, 0.25)',
            }}
          />
        )}
      />
    </Space>
  );
};

export default Demo;
```
