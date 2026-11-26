#
# PySNMP MIB module CISCO-LWAPP-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LWAPP-RF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 23999))
ciscoLwappRFCapability.setRevisions(('2012-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappRFCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappRFCapability.setLastUpdated('201202280000Z')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setDescription('Agent capabilities for CISCO-LWAPP-RF-MIB.')
ciscoLwappRFCapabilityCUWNSV7R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 23999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.3 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappRFCapabilityCUWNSV7R3.setDescription('CISCO-LWAPP-RF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-RF-CAPABILITY", ciscoLwappRFCapabilityCUWNSV7R3=ciscoLwappRFCapabilityCUWNSV7R3, PYSNMP_MODULE_ID=ciscoLwappRFCapability, ciscoLwappRFCapability=ciscoLwappRFCapability)
