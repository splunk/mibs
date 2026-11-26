#
# PySNMP MIB module CISCO-IP-UPLINK-REDIRECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-UPLINK-REDIRECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoIpUplinkRedirectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 191))
ciscoIpUplinkRedirectMIB.setRevisions(('2001-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setLastUpdated('200101220000Z')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-cat2948g-l3@cisco.com')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setDescription('This MIB module is for the configuration of  \n                Cisco IP Uplink Redirect feature.')
ciscoIpUplinkRedirectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 1))
ciurStartupStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciurStartupStatus.setStatus('current')
if mibBuilder.loadTexts: ciurStartupStatus.setDescription('The indication of whether IP Uplink Redirect\n                feature will be enabled or disabled on this\n                entity after reboot.\n\n                IP uplink redirect enables traffic between\n                Fast Ethernet interfaces to be switched through\n                the Gigabit Ethernet interface. Then ACLs applied\n                on the Gigabit Ethernet interface filter traffic\n                switched between Fast Ethernet interfaces.\n\n                Once the IP Uplink Redirect feature is enabled\n                and saved, the switch has to be rebooted for \n                it to take effect.')
ciurOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciurOperStatus.setStatus('current')
if mibBuilder.loadTexts: ciurOperStatus.setDescription('Indicates whether or not IP Uplink Redirect\n                is currently operational on this entity.')
ciscoIpUplinkRedirectMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 2))
ciscoIpUplinkRedirectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3))
ciscoIpUplinkRedirectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1))
ciscoIpUplinkRedirectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2))
ciscoIpUplinkRedirectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciscoIpUplinkRedirectMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBCompliance = ciscoIpUplinkRedirectMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIBCompliance.setDescription('The compliance statement for the Cisco \n                L3 Switch/Router IP Uplink Redirect group.')
ciscoIpUplinkRedirectMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurStartupStatus"), ("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBGroup = ciscoIpUplinkRedirectMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIBGroup.setDescription('The Object Group for IP Uplink Redirect')
mibBuilder.exportSymbols("CISCO-IP-UPLINK-REDIRECT-MIB", ciscoIpUplinkRedirectMIBNotificationPrefix=ciscoIpUplinkRedirectMIBNotificationPrefix, ciurOperStatus=ciurOperStatus, ciscoIpUplinkRedirectMIBObjects=ciscoIpUplinkRedirectMIBObjects, ciurStartupStatus=ciurStartupStatus, ciscoIpUplinkRedirectMIBCompliance=ciscoIpUplinkRedirectMIBCompliance, ciscoIpUplinkRedirectMIBCompliances=ciscoIpUplinkRedirectMIBCompliances, ciscoIpUplinkRedirectMIBGroups=ciscoIpUplinkRedirectMIBGroups, PYSNMP_MODULE_ID=ciscoIpUplinkRedirectMIB, ciscoIpUplinkRedirectMIB=ciscoIpUplinkRedirectMIB, ciscoIpUplinkRedirectMIBGroup=ciscoIpUplinkRedirectMIBGroup, ciscoIpUplinkRedirectMIBConformance=ciscoIpUplinkRedirectMIBConformance)
