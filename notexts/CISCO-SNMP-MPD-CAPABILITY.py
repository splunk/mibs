#
# PySNMP MIB module CISCO-SNMP-MPD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-MPD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
ciscoSnmpMpdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 317))
ciscoSnmpMpdCapability.setRevisions(('2008-02-11 00:00', '2006-05-27 00:00', '2004-01-30 00:00',))
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setLastUpdated('200802110000Z')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setOrganization('Cisco Systems, Inc.')
cSnmpMpdCapabilityCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setStatus('current')
cSnmpMpdCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setStatus('current')
cSnmpMpdCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-MPD-CAPABILITY", cSnmpMpdCapabilityCatOSV05R0401=cSnmpMpdCapabilityCatOSV05R0401, cSnmpMpdCapabilityACSWV03R000=cSnmpMpdCapabilityACSWV03R000, cSnmpMpdCapabilityc4710aceVA1R700=cSnmpMpdCapabilityc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpMpdCapability, ciscoSnmpMpdCapability=ciscoSnmpMpdCapability)
