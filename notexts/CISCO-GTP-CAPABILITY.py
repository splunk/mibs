#
# PySNMP MIB module CISCO-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 263))
ciscoGtpCapability.setRevisions(('2003-04-02 09:00', '2002-03-21 16:00',))
if mibBuilder.loadTexts: ciscoGtpCapability.setLastUpdated('200304020900Z')
if mibBuilder.loadTexts: ciscoGtpCapability.setOrganization('Cisco Systems, Inc.')
cGtpCapabilityV12R02Rev08YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setProductRelease('Cisco IOS 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setStatus('current')
cGtpCapabilityV12R02Rev08YY = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setProductRelease('Cisco IOS 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setStatus('current')
cGtpCapabilityV12R02Rev08YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setStatus('current')
mibBuilder.exportSymbols("CISCO-GTP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YD=cGtpCapabilityV12R02Rev08YD, ciscoGtpCapability=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YW=cGtpCapabilityV12R02Rev08YW, cGtpCapabilityV12R02Rev08YY=cGtpCapabilityV12R02Rev08YY)
