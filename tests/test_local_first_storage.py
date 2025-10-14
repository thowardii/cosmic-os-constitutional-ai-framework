"""
Tests for Local-First Storage
==============================
"""

import pytest
from pathlib import Path
from cosmic_os.storage import LocalFirstStorage, StorageBackend, SyncStatus
import tempfile


class TestLocalFirstStorage:
    """Test suite for local-first storage"""

    def setup_method(self):
        """Setup test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.storage = LocalFirstStorage(
            storage_path=Path(self.temp_dir),
            backend=StorageBackend.LOCAL_FILE,
            cloud_sync_enabled=False
        )

    def test_storage_initialization(self):
        """Test storage initializes correctly"""
        assert self.storage.storage_path.exists()
        assert self.storage.backend == StorageBackend.LOCAL_FILE
        assert self.storage.cloud_sync_enabled is False

    @pytest.mark.skip(reason="Implementation pending")
    @pytest.mark.asyncio
    async def test_write_local_first(self):
        """Test data is written locally first (constitutional requirement)"""
        metadata = await self.storage.write(
            key="test_key",
            data={"test": "data"},
            encrypt=True
        )

        assert metadata.key == "test_key"
        assert metadata.sync_status == SyncStatus.NOT_SYNCED
        assert metadata.encrypted is True

    @pytest.mark.skip(reason="Implementation pending")
    @pytest.mark.asyncio
    async def test_read_from_local(self):
        """Test reading data from local storage"""
        # Write data
        await self.storage.write(key="test", data={"value": 123})

        # Read data
        result = await self.storage.read(key="test")
        assert result == {"value": 123}

    @pytest.mark.skip(reason="Implementation pending")
    @pytest.mark.asyncio
    async def test_cloud_sync_requires_consent(self):
        """Test cloud sync requires user consent (constitutional requirement)"""
        # Storage without consent callback
        storage_no_consent = LocalFirstStorage(
            storage_path=Path(self.temp_dir),
            cloud_sync_enabled=True,
            user_consent_callback=lambda: False
        )

        # Attempt sync without consent should fail
        with pytest.raises(Exception) as exc_info:
            await storage_no_consent.sync_to_cloud()

        assert "consent" in str(exc_info.value).lower()

    @pytest.mark.skip(reason="Implementation pending")
    @pytest.mark.asyncio
    async def test_export_all_data(self):
        """Test data export (Article II, Section 7: Right to Exit)"""
        # Write some data
        await self.storage.write(key="key1", data="data1")
        await self.storage.write(key="key2", data="data2")

        # Export all data
        export_path = await self.storage.export_all(
            export_path=Path(self.temp_dir) / "export.json"
        )

        assert export_path.exists()

    def test_has_user_consent_no_callback(self):
        """Test consent check when no callback provided"""
        assert self.storage.has_user_consent() is False

    def test_has_user_consent_with_callback(self):
        """Test consent check with callback"""
        storage_with_consent = LocalFirstStorage(
            storage_path=Path(self.temp_dir),
            cloud_sync_enabled=True,
            user_consent_callback=lambda: True
        )

        assert storage_with_consent.has_user_consent() is True


class TestConstitutionalCompliance:
    """Test constitutional compliance of storage"""

    def setup_method(self):
        """Setup test fixtures"""
        self.temp_dir = tempfile.mkdtemp()

    @pytest.mark.skip(reason="Implementation pending")
    def test_rejects_cloud_first_architecture(self):
        """Test storage rejects cloud-first operations"""
        # This should raise a constitutional violation error
        # if implementation attempts to write to cloud before local
        pass

    @pytest.mark.skip(reason="Implementation pending")
    def test_functions_without_cloud(self):
        """Test storage functions fully without cloud connectivity"""
        storage = LocalFirstStorage(
            storage_path=Path(self.temp_dir),
            cloud_sync_enabled=False
        )

        # Should be able to perform all operations locally
        # without any cloud connectivity
        pass
