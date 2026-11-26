#
# PySNMP MIB module ACOS-VCS-IMAGES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-VCS-IMAGES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:31 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, NotificationType, Counter64, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
vcsImagesModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16))
if mibBuilder.loadTexts: vcsImagesModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: vcsImagesModule.setOrganization('A10 Networks, Inc.')
images = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1))
imagesOperImagesListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2), )
if mibBuilder.loadTexts: imagesOperImagesListTable.setStatus('current')
imagesOperImagesListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1), ).setIndexNames((0, "ACOS-VCS-IMAGES-MIB", "imagesOperImagesListSlotId"), (0, "ACOS-VCS-IMAGES-MIB", "imagesOperImagesListImagesListListId"))
if mibBuilder.loadTexts: imagesOperImagesListEntry.setStatus('current')
imagesOperImagesListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListSlotId.setStatus('current')
imagesOperImagesListImagesListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListImagesListListId.setStatus('current')
imagesOperImagesListType = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListType.setStatus('current')
imagesOperImagesListImagesName = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListImagesName.setStatus('current')
mibBuilder.exportSymbols("ACOS-VCS-IMAGES-MIB", images=images, imagesOperImagesListEntry=imagesOperImagesListEntry, PYSNMP_MODULE_ID=vcsImagesModule, vcsImagesModule=vcsImagesModule, imagesOperImagesListImagesName=imagesOperImagesListImagesName, imagesOperImagesListImagesListListId=imagesOperImagesListImagesListListId, imagesOperImagesListType=imagesOperImagesListType, imagesOperImagesListTable=imagesOperImagesListTable, imagesOperImagesListSlotId=imagesOperImagesListSlotId)
