#
# PySNMP MIB module CISCO-DMN-DSG-DECODE-ENABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-DECODE-ENABLE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-DMN-DSG-DECODE-ENABLE-MIB", PYSNMP_MODULE_ID=ciscoDSGDecodeEnable, decodeType=decodeType, decodeEnable=decodeEnable, ciscoDSGDecodeEnable=ciscoDSGDecodeEnable, decodeEnableEntry=decodeEnableEntry, decodeEnableTable=decodeEnableTable)
