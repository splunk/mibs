#
# PySNMP MIB module CISCO-DMN-DSG-DECODE-ENABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-DECODE-ENABLE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGDecodeEnable = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13))
ciscoDSGDecodeEnable.setRevisions(('2010-08-30 06:00', '2009-12-07 12:00',))
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setLastUpdated('201008300600Z')
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setOrganization('Cisco Systems, Inc.')
decodeEnableTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1), )
if mibBuilder.loadTexts: decodeEnableTable.setStatus('current')
decodeEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DECODE-ENABLE-MIB", "decodeType"))
if mibBuilder.loadTexts: decodeEnableEntry.setStatus('current')
decodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("video", 1), ("audio1", 2), ("audio2", 3), ("audio3", 4), ("audio4", 5), ("vbi", 6), ("data", 7), ("mpe1", 8), ("mpe2", 9), ("mpe3", 10), ("mpe4", 11), ("mpe5", 12), ("stt", 13), ("dpi", 14))))
if mibBuilder.loadTexts: decodeType.setStatus('current')
decodeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: decodeEnable.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DECODE-ENABLE-MIB", decodeEnable=decodeEnable, PYSNMP_MODULE_ID=ciscoDSGDecodeEnable, decodeType=decodeType, decodeEnableEntry=decodeEnableEntry, ciscoDSGDecodeEnable=ciscoDSGDecodeEnable, decodeEnableTable=decodeEnableTable)
